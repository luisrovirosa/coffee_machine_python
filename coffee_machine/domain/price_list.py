from coffee_machine.domain.drink_type import DrinkType


class PriceList:
    def __init__(self):
        self.prices = {
            DrinkType.Coffee: 60,
            DrinkType.Tea: 40,
            DrinkType.Chocolate: 50,
        }

    def price_of(self, drink_type: DrinkType) -> int:
        return self.prices.get(drink_type)