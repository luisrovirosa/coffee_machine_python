from coffee_machine.domain.drink import Drink
from coffee_machine.domain.drink_maker import DrinkMaker
from coffee_machine.domain.drink_type import DrinkType


class CoffeeMachine:
    def __init__(self, drink_maker: DrinkMaker) -> None:
        self.drink_maker = drink_maker
        self.sugar_level = 0

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

    def _prepare_drink(self, drink: DrinkType):
        self.drink_maker.prepare(Drink(drink=drink, sugar=self.sugar_level))
        self.sugar_level = 0
