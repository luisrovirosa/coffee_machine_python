from coffee_machine.domain.drink import Drink
from coffee_machine.domain.drink_type import DrinkType
from coffee_machine.infrastructure.cheap_drink_maker import CheapDrinkMaker
from coffee_machine.infrastructure.cheap_drink_maker_adapter import CheapDrinkMakerAdapter


class CoffeeMachine:
    def __init__(self, drink_maker: CheapDrinkMaker) -> None:
        self.drink_maker = drink_maker
        self.drink_maker_adapter = CheapDrinkMakerAdapter(drink_maker)
        self.current_drink = Drink()
        self.sugar_level = 0

    def prepare_coffee(self):
        self.current_drink.drink = DrinkType.Coffee
        self._prepare_drink()

    def prepare_tea(self):
        self.current_drink.drink = DrinkType.Tea
        self._prepare_drink()

    def prepare_chocolate(self):
        self.current_drink.drink = DrinkType.Chocolate
        self._prepare_drink()

    def add_one_sugar(self):
        self.sugar_level = 1

    def add_two_sugar(self):
        self.sugar_level = 2

    def _prepare_drink(self):
        self.current_drink.sugar = self.sugar_level
        self.drink_maker_adapter.prepare(self.current_drink)
        self.sugar_level = 0
