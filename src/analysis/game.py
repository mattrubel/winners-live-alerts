from src.analysis.head_to_heads import HeadToHeads
from src.analysis.spreads import Spreads
from src.analysis.totals import Totals


class Game:
    def __init__(self, game_id: str, home_team: str, away_team: str, commence_time: str):
        self.game_id = game_id
        self.home_team = home_team
        self.away_team = away_team
        self.commence_time = commence_time

        self.totals = Totals()
        self.spreads = Spreads()
        self.head_to_heads = HeadToHeads()

    def add_market(self, book_name: str, market_key: str, outcomes: list):
        if market_key == "totals":
            self.add_total(book_name, outcomes)
        elif market_key == "h2h":
            self.add_h2h(book_name, outcomes)
        elif market_key == "spreads":
            self.add_spreads(book_name, outcomes)
        else:
            raise RuntimeError("Invalid market_key")

    def add_total(self, book_name, outcomes):
        over_total = None
        over_price = None
        under_total = None
        under_price = None

        for outcome in outcomes:
            if outcome.name == "Over":
                over_total = outcome.point
                over_price = outcome.price
            elif outcome.name == "Under":
                under_total = outcome.point
                under_price = outcome.price

        assert over_total is not None
        assert over_price is not None
        assert under_total is not None
        assert under_price is not None

        self.totals.add_total(over_total, under_total, over_price, under_price, book_name)

    def add_h2h(self, book_name, outcomes):
        home_price = None
        away_price = None
        for outcome in outcomes:
            if outcome.name == self.home_team:
                home_price = outcome.price
            elif outcome.name == self.away_team:
                away_price = outcome.price

        assert home_price is not None
        assert away_price is not None

        self.head_to_heads.add_h2h(away_price, home_price, book_name)

    def add_spreads(self, book_name, outcomes):
        home_spread = None
        away_spread = None
        home_price = None
        away_price = None

        for outcome in outcomes:
            if outcome.name == self.home_team:
                home_spread = outcome.point
                home_price = outcome.price
            elif outcome.name == self.away_team:
                away_spread = outcome.point
                away_price = outcome.price

        assert home_price is not None
        assert home_spread is not None
        assert away_price is not None
        assert away_spread is not None

        self.spreads.add_spread(home_price, home_spread, away_price, away_spread, book_name)
