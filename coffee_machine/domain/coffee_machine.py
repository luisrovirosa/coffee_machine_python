from coffee_machine.domain.beverage_quantity_checker import BeverageQuantityChecker
from coffee_machine.domain.drink import Drink
from coffee_machine.domain.drink_maker import DrinkMaker
from coffee_machine.domain.drink_type import DrinkType
from coffee_machine.domain.price_list import PriceList
from coffee_machine.domain.printer import Printer


class CoffeeMachine:
    def __init__(self, drink_maker: DrinkMaker, printer: Printer, beverage_quantity_checker: BeverageQuantityChecker) -> None:
        self.price_list = PriceList({
            DrinkType.Coffee: 60,
            DrinkType.Tea: 40,
            DrinkType.Chocolate: 50,
            DrinkType.Orange: 60,
        })
        self.drink_maker = drink_maker
        self.printer = printer
        self.beverage_quantity_checker = beverage_quantity_checker
        self.sugar_level = 0
        self.money_in_cents = 0
        self.extra_hot = False
        self.sold_products = {
            DrinkType.Coffee: 0,
            DrinkType.Tea: 0,
            DrinkType.Chocolate: 0,
            DrinkType.Orange: 0,
        }

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

    def print_report(self):
        for drink_type in DrinkType:
            self.printer.print(f'{drink_type.name}: {self.sold_products[drink_type]}')
        earnings_per_products = [self.price_list.price_of(drink_type) * self.sold_products[drink_type] for drink_type in DrinkType]
        amount_made =  sum(earnings_per_products)
        self.printer.print(f'The amount of money made is: {amount_made}')

    def _prepare_drink(self, drink_type: DrinkType) -> None:
        if self.beverage_quantity_checker.is_empty(drink_type):
            self.drink_maker.communicate(f'There is a shortage of {drink_type.name}')
            return

        missing_money = self.price_list.price_of(drink_type) - self.money_in_cents
        if missing_money > 0:
            self.drink_maker.communicate(f'You need to add {missing_money} cents')
            return

        self.drink_maker.prepare(Drink(type=drink_type, sugar=self.sugar_level, extra_hot=self.extra_hot))
        self.sold_products[drink_type] += 1
        self.sugar_level = 0
        self.money_in_cents = 0

