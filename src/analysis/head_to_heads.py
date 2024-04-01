class HeadToHeads:

    def __init__(self):
        self.home_prices = []
        self.away_prices = []
        self.books = []

    def add_h2h(self, home_price: float, away_price: float, book: str):
        self.home_prices.append(home_price)
        self.away_prices.append(away_price)
        self.books.append(book)

    def price_differences(self, price_difference: float):
        if abs(max(self.home_prices) - max(self.away_prices)) >= price_difference:
            return True

        return False

    def direct_arbitrage(self) -> [None, tuple]:
        max_home_price = max(self.home_prices)
        max_away_price = max(self.away_prices)
        max_home_implied = 1 / max_home_price
        max_away_implied = 1 / max_away_price

        if max_away_implied + max_home_implied < 1:
            away_book = self.books[self.away_prices.index(max_away_price)]
            home_book = self.books[self.home_prices.index(max_home_price)]

            return home_book, away_book

        return None
