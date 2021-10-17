import pytest
from doublex import Spy
from doublex_expects import have_been_called_with, have_been_called
from expects import expect

from coffee_machine import CoffeeMachine
from coffee_machine.domain.drink import Drink
from coffee_machine.domain.drink_maker import DrinkMaker
from coffee_machine.domain.drink_type import DrinkType


class TestCoffeeMachinePreparesProducts:

    def setup(self):
        self.adapter = Spy(DrinkMaker)
        self.coffee_machine = CoffeeMachine(self.adapter, Spy())
        self.coffee_machine.add_money(ENOUGH_MONEY)

    def test_prepare_a_coffee_without_sugar_when_coffee_is_pressed(self):
        self.coffee_machine.prepare_coffee()

        expect(self.adapter.prepare).to(have_been_called_with(Drink(DrinkType.Coffee, 0, False)))

    def test_prepare_a_tea_without_sugar_when_tea_is_pressed(self):
        self.coffee_machine.prepare_tea()

        expect(self.adapter.prepare).to(have_been_called_with(Drink(DrinkType.Tea, 0, False)))

    def test_prepare_a_chocolate_without_sugar_when_chocolate_is_pressed(self):
        self.coffee_machine.prepare_chocolate()

        expect(self.adapter.prepare).to(have_been_called_with(Drink(DrinkType.Chocolate, 0, False)))

    def test_prepare_a_orange_without_sugar_when_orange_is_pressed(self):
        self.coffee_machine.prepare_orange()

        expect(self.adapter.prepare).to(have_been_called_with(Drink(DrinkType.Orange, 0, False)))

    def test_prepare_a_coffee_with_one_sugar_and_stick_when_select_one_sugar_and_coffee_is_pressed(self):
        self.coffee_machine.add_one_sugar()
        self.coffee_machine.prepare_coffee()

        expect(self.adapter.prepare).to(have_been_called_with(Drink(DrinkType.Coffee, 1, False)))

    def test_prepare_a_coffee_with_two_sugar_and_stick_when_select_two_sugar_and_coffee_is_pressed(self):
        self.coffee_machine.add_two_sugar()
        self.coffee_machine.prepare_coffee()

        expect(self.adapter.prepare).to(have_been_called_with(Drink(DrinkType.Coffee, 2, False)))

    def test_prepare_a_tea_with_one_sugar_and_stick_when_select_one_sugar_and_tea_is_pressed(self):
        self.coffee_machine.add_one_sugar()
        self.coffee_machine.prepare_tea()

        expect(self.adapter.prepare).to(have_been_called_with(Drink(DrinkType.Tea, 1, False)))

    def test_prepare_a_tea_with_two_sugar_and_stick_when_select_one_sugar_and_tea_is_pressed(self):
        self.coffee_machine.add_two_sugar()
        self.coffee_machine.prepare_tea()

        expect(self.adapter.prepare).to(have_been_called_with(Drink(DrinkType.Tea, 2, False)))

    def test_prepare_a_chocolate_with_one_sugar_and_stick_when_select_one_sugar_and_chocolate_is_pressed(self):
        self.coffee_machine.add_one_sugar()
        self.coffee_machine.prepare_chocolate()

        expect(self.adapter.prepare).to(have_been_called_with(Drink(DrinkType.Chocolate, 1, False)))

    def test_prepare_a_chocolate_with_two_sugar_and_stick_when_select_one_sugar_and_chocolate_is_pressed(self):
        self.coffee_machine.add_two_sugar()
        self.coffee_machine.prepare_chocolate()

        expect(self.adapter.prepare).to(have_been_called_with(Drink(DrinkType.Chocolate, 2, False)))

    def test_sugar_level_is_not_related_to_previous_drinks(self):
        self.coffee_machine.add_two_sugar()
        self.coffee_machine.prepare_coffee()

        self.coffee_machine.add_money(ENOUGH_MONEY)
        self.coffee_machine.prepare_coffee()

        expect(self.adapter.prepare).to(have_been_called_with(Drink(DrinkType.Coffee, 0, False)))


def prepare_coffee(coffee_machine: CoffeeMachine):
    return coffee_machine.prepare_coffee()


def prepare_tea(coffee_machine: CoffeeMachine):
    return coffee_machine.prepare_tea()


def prepare_chocolate(coffee_machine: CoffeeMachine):
    return coffee_machine.prepare_chocolate()


def prepare_orange(coffee_machine: CoffeeMachine):
    return coffee_machine.prepare_orange()


CHOCOLATE_PRICE = 50
TEA_PRICE = 40
COFFEE_PRICE = 60
ORANGE_PRICE = 60
ENOUGH_MONEY = 100

class TestCoffeeMachineGoingIntoBusiness:

    def setup(self):
        self.adapter = Spy(DrinkMaker)
        self.coffee_machine = CoffeeMachine(self.adapter, Spy())

    @pytest.mark.parametrize('prepare_drink', [
        (prepare_coffee),
        (prepare_tea),
        (prepare_chocolate),
        (prepare_orange),
    ])
    def test_drinks_are_not_served_if_no_money_is_added(self, prepare_drink: callable):
        prepare_drink(self.coffee_machine)

        expect(self.adapter.prepare).not_to(have_been_called)

    @pytest.mark.parametrize('prepare_drink,money', [
        (prepare_coffee, COFFEE_PRICE),
        (prepare_tea, TEA_PRICE),
        (prepare_chocolate, CHOCOLATE_PRICE),
        (prepare_orange, ORANGE_PRICE),
        (prepare_coffee, ENOUGH_MONEY),
        (prepare_tea, ENOUGH_MONEY),
        (prepare_chocolate, ENOUGH_MONEY),
        (prepare_orange, ENOUGH_MONEY),
    ])
    def test_drinks_are_prepared_when_there_is_enough_money(self, prepare_drink: callable, money: int):
        self.coffee_machine.add_money(money)
        prepare_drink(self.coffee_machine)

        expect(self.adapter.prepare).to(have_been_called)

    @pytest.mark.parametrize('prepare_drink', [
        (prepare_coffee),
        (prepare_tea),
        (prepare_chocolate),
        (prepare_orange),
    ])
    def test_no_message_is_displayed_when_there_is_enough_money(self, prepare_drink: callable):
        self.coffee_machine.add_money(ENOUGH_MONEY)
        prepare_drink(self.coffee_machine)

        expect(self.adapter.communicate).not_to(have_been_called)

    @pytest.mark.parametrize('prepare_drink,money,missing_cents', [
        (prepare_coffee, 0, COFFEE_PRICE),
        (prepare_coffee, 59, 1),
        (prepare_chocolate, 0, CHOCOLATE_PRICE),
        (prepare_tea, 0, TEA_PRICE),
        (prepare_orange, 0, ORANGE_PRICE),
    ])
    def test_shows_the_missing_money_when_there_is_no_enough_money(self, prepare_drink: callable, money: int,
                                                                   missing_cents: int):
        self.coffee_machine.add_money(money)
        prepare_drink(self.coffee_machine)

        expect(self.adapter.communicate).to(have_been_called_with(f'You need to add {missing_cents} cents'))

    @pytest.mark.parametrize('prepare_drink,missing_cents', [
        (prepare_coffee, COFFEE_PRICE),
        (prepare_tea, TEA_PRICE),
        (prepare_chocolate, CHOCOLATE_PRICE),
        (prepare_orange, ORANGE_PRICE),
    ])
    def test_show_the_price_of_the_drink_when_no_money_is_added(self, prepare_drink: callable, missing_cents: int):
        prepare_drink(self.coffee_machine)

        expect(self.adapter.communicate).to(have_been_called_with(f'You need to add {missing_cents} cents'))

    @pytest.mark.parametrize('prepare_drink,missing_cents', [
        (prepare_coffee, COFFEE_PRICE),
        (prepare_tea, TEA_PRICE),
        (prepare_chocolate, CHOCOLATE_PRICE),
        (prepare_orange, ORANGE_PRICE),
    ])
    def test_each_user_needs_to_add_money(self, prepare_drink: callable, missing_cents: int):
        self.coffee_machine.add_money(ENOUGH_MONEY)
        prepare_drink(self.coffee_machine)

        prepare_drink(self.coffee_machine)

        expect(self.adapter.prepare).to(have_been_called.once)
        expect(self.adapter.communicate).to(have_been_called_with(f'You need to add {missing_cents} cents'))


class TestCoffeeMachineExtraHot:
    @pytest.mark.parametrize('drink_type,prepare_drink', [
        (DrinkType.Coffee, prepare_coffee),
        (DrinkType.Tea, prepare_tea),
        (DrinkType.Chocolate, prepare_chocolate),
    ])
    def test_drinks_can_be_extra_hot(self, drink_type: DrinkType, prepare_drink: callable):
        drink_maker = Spy(DrinkMaker)
        coffee_machine = CoffeeMachine(drink_maker, Spy())

        coffee_machine.add_money(ENOUGH_MONEY)
        coffee_machine.extra_hot_drink()
        prepare_drink(coffee_machine)

        expect(drink_maker.prepare).to(have_been_called_with(Drink(drink_type, 0, True)))

    def test_orange_cannot_be_extra_hot(self):
        drink_maker = Spy(DrinkMaker)
        coffee_machine = CoffeeMachine(drink_maker, Spy())

        coffee_machine.add_money(ENOUGH_MONEY)
        coffee_machine.extra_hot_drink()
        coffee_machine.prepare_orange()

        expect(drink_maker.prepare).to(have_been_called_with(Drink(DrinkType.Orange, 0, False)))


class TestCoffeeMachineMakingMoney:

    @pytest.mark.parametrize('prepare_drinks, expected_report_line', [
        ([prepare_coffee], 'Coffee: 1'),
        ([prepare_tea], 'Tea: 1'),
        ([prepare_chocolate], 'Chocolate: 1'),
        ([prepare_orange], 'Orange: 1'),
        ([prepare_coffee, prepare_coffee], 'Coffee: 2'),
        ([prepare_tea, prepare_tea], 'Tea: 2'),
        ([prepare_chocolate, prepare_chocolate], 'Chocolate: 2'),
        ([prepare_orange, prepare_orange], 'Orange: 2'),
        ([prepare_coffee, prepare_coffee, prepare_orange], 'Coffee: 2'),
        ([prepare_coffee, prepare_coffee, prepare_orange], 'Orange: 1'),
    ])
    def test_calculate_the_amount_of_drinks_sold(self, prepare_drinks: list, expected_report_line: str):
        printer = Spy()
        coffee_machine = CoffeeMachine(Spy(), printer)
        for prepare_drink in prepare_drinks:
            coffee_machine.add_money(ENOUGH_MONEY)
            prepare_drink(coffee_machine)

        coffee_machine.print_report()

        expect(printer.print).to(have_been_called_with(expected_report_line))

    @pytest.mark.parametrize('prepare_drinks, expected_money', [
        ([prepare_coffee], COFFEE_PRICE),
        ([prepare_coffee, prepare_coffee], 2 * COFFEE_PRICE),
        ([prepare_tea], TEA_PRICE),
        ([prepare_chocolate], CHOCOLATE_PRICE),
        ([prepare_orange], ORANGE_PRICE),
        ([prepare_coffee, prepare_tea], COFFEE_PRICE + TEA_PRICE),
    ])
    def test_calculate_the_amount_of_money_made(self, prepare_drinks: list, expected_money: int):
        printer = Spy()
        coffee_machine = CoffeeMachine(Spy(), printer)
        for prepare_drink in prepare_drinks:
            coffee_machine.add_money(ENOUGH_MONEY)
            prepare_drink(coffee_machine)

        coffee_machine.print_report()

        expect(printer.print).to(have_been_called_with(f'The amount of money made is: {expected_money}'))
