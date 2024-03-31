from src.analysis.head_to_heads import HeadToHeads


class TestHeadToHeads:
    def test_direct_arbitrage_true(self):
        obj = HeadToHeads()

        obj.add_h2h(1.91, 1.91, "book1")
        obj.add_h2h(1.82, 2.0, "book2")
        obj.add_h2h(1.71, 2.2, "book3")

        assert obj.direct_arbitrage()

    def test_direct_arbitrage_false(self):
        obj = HeadToHeads()

        obj.add_h2h(1.91, 1.91, "book1")
        obj.add_h2h(1.91, 1.91, "book2")
        obj.add_h2h(1.91, 1.91, "book3")

        assert not obj.direct_arbitrage()

    def test_price_difference_true(self):
        obj = HeadToHeads()

        obj.add_h2h(1.91, 1.91, "book1")
        obj.add_h2h(1.82, 2.0, "book2")
        obj.add_h2h(1.71, 2.3, "book3")

        assert obj.price_differences(0.25)

    def test_price_difference_false(self):
        obj = HeadToHeads()

        obj.add_h2h(1.91, 1.91, "book1")
        obj.add_h2h(1.91, 1.91, "book2")
        obj.add_h2h(1.91, 1.91, "book3")

        assert not obj.price_differences(0.25)
