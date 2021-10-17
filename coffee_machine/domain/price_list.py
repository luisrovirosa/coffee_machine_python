from coffee_machine.domain.drink_type import DrinkType


class PriceList:
    def __init__(self, prices: dict):
        if not all(drink_type in prices for drink_type in DrinkType):
            raise Exception(f'Missing price for {type}')
        self.prices = prices

    def price_of(self, drink_type: DrinkType) -> int:
        return self.prices.get(drink_type)