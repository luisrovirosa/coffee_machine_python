from coffee_machine.domain.drink_type import DrinkType
from coffee_machine.domain.price_list import PriceList


class TestPriceList:
    price_for_all_drinks = {
        DrinkType.Coffee: 1,
        DrinkType.Tea: 1,
        DrinkType.Chocolate: 1,
    }

    def test_can_be_created_with_all_drink_type_prices(self):
        PriceList(self.price_for_all_drinks)
