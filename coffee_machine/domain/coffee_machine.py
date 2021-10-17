from coffee_machine.domain.drink import Drink
from coffee_machine.domain.drink_maker import DrinkMaker
from coffee_machine.domain.drink_type import DrinkType
from coffee_machine.domain.price_list import PriceList


class CoffeeMachine:
    def __init__(self, drink_maker: DrinkMaker) -> None:
        self.price_list = PriceList({
            DrinkType.Coffee: 60,
            DrinkType.Tea: 40,
            DrinkType.Chocolate: 50,
            DrinkType.Orange: 60,
        })
        self.drink_maker = drink_maker
        self.sugar_level = 0
        self.money_in_cents = 0
        self.extra_hot = False

    def prepare_coffee(self):
        self._prepare_drink(DrinkType.Coffee)

    def prepare_tea(self):
        self._prepare_drink(DrinkType.Tea)

    def prepare_chocolate(self):
        self._prepare_drink(DrinkType.Chocolate)

    def prepare_orange(self):
        self._prepare_drink(DrinkType.Orange)

    def add_one_sugar(self):
        self.sugar_level = 1

    def add_two_sugar(self):
        self.sugar_level = 2

    def add_money(self, money_in_cents: int):
        self.money_in_cents = money_in_cents

    def extra_hot_drink(self) -> None:
        self.extra_hot = True

    def _prepare_drink(self, drink_type: DrinkType):
        missing_money = self.price_list.price_of(drink_type) - self.money_in_cents
        if missing_money <= 0:
            self.drink_maker.prepare(Drink(type=drink_type, sugar=self.sugar_level, extra_hot=self.extra_hot))
            self.sugar_level = 0
            self.money_in_cents = 0
        else:
            self.drink_maker.communicate(f'You need to add {missing_money} cents')

