from coffee_machine.domain.drink import Drink
from coffee_machine.domain.drink_type import DrinkType
from coffee_machine.infrastructure.cheap_drink_maker import CheapDrinkMaker
from coffee_machine.infrastructure.cheap_drink_maker_adapter import CheapDrinkMakerAdapter


class CoffeeMachine:
    def __init__(self, drink_maker: CheapDrinkMaker) -> None:
        self.drink_maker_adapter = CheapDrinkMakerAdapter(drink_maker)
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
        self.drink_maker_adapter.prepare(Drink(drink=drink, sugar=self.sugar_level))
        self.sugar_level = 0
