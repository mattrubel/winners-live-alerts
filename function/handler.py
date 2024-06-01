import argparse
import boto3
import json
from src.analysis.game import Game
from src.alerts.alert import Alert


def event_handler(event: dict, ctx=None):
    print(event)
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']

    print(bucket)
    print(key)

    game_list = get_s3_file(bucket, key)
    games = load_games(game_list)
    print(len(games))
    if len(games) == 0:
        print("No games that haven't started yet.")
    reportable_events = analyze_games(games)

    if len(reportable_events) > 0:
        send_reports(reportable_events)


def get_s3_file(bucket: str, key: str) -> list:
    s3 = boto3.client('s3')
    response = s3.get_object(Bucket=bucket, Key=key)
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
    reports_to_send = []
    for report in reports:
        if 'arb' in report[1]:
            report_msg = f"game_id: {report[0]}, type {report[1]}, book1 {report[2][0]}, book2: {report[2][1]}"
            reports_to_send.append(
                report_msg
            )

    final_message = "\n".join(reports_to_send)

    alert = Alert("arn:aws:sns:us-east-1:597426459950:winners-alerts-topic")

    alert.send_notification("Report", final_message)


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

    bucket = s3_path_.split("/")[2]
    path = "/".join(s3_path_.split("/")[3:])
    print(bucket)
    print(path)

    event_ = {
        "Records": [
            {
                's3': {
                    'bucket': {
                        "name": bucket
                    },
                    'object': {
                        "key": path
                    }
                }
            }
        ]
    }
    event_handler(event_)
