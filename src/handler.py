import argparse
import boto3
import json

from src.analysis.game import Game


def event_handler(event: dict, ctx=None):
    game_list = get_s3_file(event['s3_path'])
    games = load_games(game_list)
    print(len(games))
    if len(games) == 0:
        print("No games that haven't started yet.")
    reportable_events = analyze_games(games)

    if len(reportable_events) > 0:
        send_reports(reportable_events)


def get_s3_file(s3_path: str) -> list:
    s3 = boto3.client('s3')
    split_path = s3_path.split("/", 3)
    response = s3.get_object(Bucket=split_path[2], Key=split_path[3])
    json_content = response['Body'].read().decode('utf-8')

    # Parse the JSON content into a dictionary
    data_list = json.loads(json_content)
    return data_list


def load_games(game_list: list) -> list:
    games = []
    for game_dict in game_list:
        game = Game(
            game_dict['id'],
            game_dict['home_team'],
            game_dict['away_team'],
            game_dict['commence_time']
        )

        books = game_dict['bookmakers']
        added_market = False
        for book in books:

            # only want games that haven't been updated before commence time
            if book['last_update'] > game.commence_time:
                continue

            for market in book['markets']:
                added_market = True
                game.add_market(
                    book['key'],
                    market['key'],
                    market['outcomes']
                )

        # ensure not adding game where no valid markets exist
        if added_market:
            games.append(game)

    return games


def analyze_games(games: list) -> list:
    reportable_events = []

    for game in games:
        game_id, analyses = game.execute_analyses()

        for key in analyses.keys():
            if analyses[key]:
                reportable_events.append((game_id, key, analyses[key]))

    return reportable_events


def send_reports(reports: list):
    # will eventually host SNS logic
    print("Reportable game ids:")
    for report in reports:
        print(report)


def parse_args() -> dict:
    parser = argparse.ArgumentParser()
    parser.add_argument("--s3-path", help="Input File S3 path")
    args = parser.parse_args()
    return {
        "s3_path": args.s3_path
    }


if __name__ == "__main__":
    args_ = parse_args()
    s3_path_ = args_['s3_path']
    event_ = {
        "s3_path": s3_path_
    }
    event_handler(event_)
