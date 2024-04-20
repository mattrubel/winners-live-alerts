class Totals:

    def __init__(self):
        self.over_totals = []
        self.under_totals = []
        self.over_prices = []
        self.under_prices = []
        self.books = []

    def add_total(self, over_total: float, under_total: float, over_price: float, under_price: float, book: str):
        self.over_totals.append(over_total)
        self.under_totals.append(under_total)
        self.over_prices.append(over_price)
        self.under_prices.append(under_price)
        self.books.append(book)
