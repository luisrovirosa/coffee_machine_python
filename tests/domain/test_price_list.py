from expects import raise_error, expect

from coffee_machine.domain.drink_type import DrinkType
from coffee_machine.domain.price_list import PriceList


class TestPriceList:
    def setup(self):
        self.price_for_all_drinks = {
            DrinkType.Coffee: 1,
            DrinkType.Tea: 1,
            DrinkType.Chocolate: 1,
            DrinkType.Orange: 1,
        }

    def test_can_be_created_with_all_drink_type_prices(self):
        PriceList(self.price_for_all_drinks)

    def test_fail_when_missing_price_for_a_product(self):
        del(self.price_for_all_drinks[DrinkType.Coffee])

        expect(lambda : PriceList(self.price_for_all_drinks)).to(raise_error)
