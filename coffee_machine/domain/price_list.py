from coffee_machine.domain.drink_type import DrinkType


class PriceList:
    def price_of(self, drink_type: DrinkType) -> int:
        prices = {
            DrinkType.Coffee: 60,
            DrinkType.Tea: 40,
            DrinkType.Chocolate: 50,
        }
        return prices.get(drink_type)