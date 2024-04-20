class HeadToHeads:

    def __init__(self):
        self.home_prices = []
        self.away_prices = []
        self.books = []

    def add_h2h(self, home_price: float, away_price: float, book: str):
        self.home_prices.append(home_price)
        self.away_prices.append(away_price)
        self.books.append(book)

    def price_differences(self, price_difference: float) -> [dict, None]:
        max_home_price = max(self.home_prices)
        max_away_price = max(self.away_prices)

        min_home_price = min(self.home_prices)
        min_away_price = min(self.away_prices)

        if max_home_price - min_home_price >= price_difference:
            min_book = self.books[self.home_prices.index(min_home_price)]
            max_book = self.books[self.home_prices.index(max_home_price)]
            return min_book, max_book

        if max_away_price - min_away_price >= price_difference:
            min_book = self.books[self.away_prices.index(min_away_price)]
            max_book = self.books[self.away_prices.index(max_away_price)]
            return min_book, max_book

        return None

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
