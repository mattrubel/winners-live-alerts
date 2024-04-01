from src.analysis.head_to_heads import HeadToHeads


class TestHeadToHeads:
    def test_direct_arbitrage_exists(self):
        obj = HeadToHeads()

        obj.add_h2h(1.91, 1.91, "book1")
        obj.add_h2h(1.82, 2.0, "book2")
        obj.add_h2h(1.71, 2.2, "book3")

        direct_arb = obj.direct_arbitrage()

        assert direct_arb is not None

        # test book with highest home odds
        assert direct_arb[0] == "book1"

        # test book with highest away odds
        assert direct_arb[1] == "book3"

    def test_direct_arbitrage_none(self):
        obj = HeadToHeads()

        obj.add_h2h(1.91, 1.91, "book1")
        obj.add_h2h(1.91, 1.91, "book2")
        obj.add_h2h(1.91, 1.91, "book3")

        assert obj.direct_arbitrage() is None

    def test_price_difference_exists(self):
        obj = HeadToHeads()

        obj.add_h2h(1.91, 1.91, "book1")
        obj.add_h2h(1.82, 2.0, "book2")
        obj.add_h2h(1.71, 2.3, "book3")

        price_diff = obj.price_differences(0.25)
        assert price_diff is not None
        assert price_diff[0] == "book1"
        assert price_diff[1] == "book3"

    def test_price_difference_None(self):
        obj = HeadToHeads()

        obj.add_h2h(1.91, 1.91, "book1")
        obj.add_h2h(1.91, 1.91, "book2")
        obj.add_h2h(1.91, 1.91, "book3")

        assert obj.price_differences(0.25) is None
