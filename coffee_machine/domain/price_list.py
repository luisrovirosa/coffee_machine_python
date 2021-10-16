from coffee_machine.domain.drink_type import DrinkType


class PriceList:
    def __init__(self, prices: dict):
        self.prices = prices

    def price_of(self, drink_type: DrinkType) -> int:
        return self.prices.get(drink_type)