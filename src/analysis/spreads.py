class Spreads:

    def __init__(self):
        self.home_spreads = []
        self.away_spreads = []
        self.home_prices = []
        self.away_prices = []
        self.books = []

    def add_spread(self, home_prices: float, home_spreads: float, away_prices: float, away_spreads: float, book: str):
        self.home_prices.append(home_prices)
        self.home_spreads.append(home_spreads)
        self.away_prices.append(away_prices)
        self.away_spreads.append(away_spreads)
        self.books.append(book)
