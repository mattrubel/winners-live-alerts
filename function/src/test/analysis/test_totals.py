from src.analysis.totals import Totals


class TestTotals:
    def test_add_totals(self):
        obj = Totals()
        obj.add_total(9, 9, 1.91, 1.91, "book1")
        obj.add_total(9.5, 9.5, 1.91, 1.91, "book2")
        obj.add_total(9, 9, 1.91, 1.91, "book3")

        assert len(obj.over_prices) == 3
        assert len(obj.under_prices) == 3
        assert len(obj.over_totals) == 3
        assert len(obj.under_totals) == 3
        assert len(obj.books) == 3
