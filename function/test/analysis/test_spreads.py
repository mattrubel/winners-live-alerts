from function.src.analysis.spreads import Spreads


class TestSpreads:
    def test_add_spread(self):
        obj = Spreads()
        obj.add_spread(1.91, -2.5, 1.91, 2.5, "book1")
        obj.add_spread(1.87, -2.5, 1.95, 2.5, "book2")

        assert len(obj.home_spreads) == 2
        assert len(obj.away_spreads) == 2
        assert len(obj.home_prices) == 2
        assert len(obj.away_prices) == 2
