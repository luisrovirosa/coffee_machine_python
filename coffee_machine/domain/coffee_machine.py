from coffee_machine.domain.drink import Drink
from coffee_machine.domain.drink_maker import DrinkMaker
from coffee_machine.domain.drink_type import DrinkType


class CoffeeMachine:
    def __init__(self, drink_maker: DrinkMaker) -> None:
        self.drink_maker = drink_maker
        self.sugar_level = 0
        self.money_in_cents = 0

    def prepare_coffee(self):
        self._prepare_drink(DrinkType.Coffee)

    def prepare_tea(self):
        self._prepare_drink(DrinkType.Tea)

    def prepare_chocolate(self):
        self._prepare_drink(DrinkType.Chocolate)

    def add_one_sugar(self):
        self.sugar_level = 1

    def add_two_sugar(self):
        self.sugar_level = 2

    def add_money(self, money_in_cents: int):
        self.money_in_cents = money_in_cents

    def _prepare_drink(self, drink_type: DrinkType):
        missing_money = self._drink_price(drink_type) - self.money_in_cents
        if missing_money <= 0:
            self.drink_maker.prepare(Drink(type=drink_type, sugar=self.sugar_level))
            self.sugar_level = 0
            self.money_in_cents = 0
        else:
            self.drink_maker.communicate(f'You need to add {missing_money} cents')

    @staticmethod
    def _drink_price(drink_type: DrinkType):
        prices = {
            DrinkType.Coffee: 60,
            DrinkType.Tea: 40,
            DrinkType.Chocolate: 50,
        }
        return prices.get(drink_type,100)
