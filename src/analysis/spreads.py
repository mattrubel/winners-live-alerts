class Spreads:

    def __init__(self):
        self.home_spreads = []
        self.away_spreads = []
        self.home_prices = []
        self.away_prices = []
        self.books = []

    def add_spread(self, home_price: float, home_spread: float, away_price: float, away_spread: float, book: str):
        self.home_prices.append(home_price)
        self.home_spreads.append(home_spread)
        self.away_prices.append(away_price)
        self.away_spreads.append(away_spread)
        self.books.append(book)
