import pytest
from doublex import Spy
from doublex_expects import have_been_called_with, have_been_called
from expects import expect

from coffee_machine import CoffeeMachine
from coffee_machine.infrastructure.cheap_drink_maker import CheapDrinkMaker
from coffee_machine.infrastructure.cheap_drink_maker_adapter import CheapDrinkMakerAdapter


class TestCoffeeMachinePreparesProducts:

    def setup(self):
        self.drink_maker = Spy(CheapDrinkMaker)
        self.adapter = CheapDrinkMakerAdapter(self.drink_maker)
        self.coffee_machine = CoffeeMachine(self.adapter)
        self.coffee_machine.add_money(100)

    def test_prepare_a_coffee_without_sugar_when_coffee_is_pressed(self):
        self.coffee_machine.prepare_coffee()

        expect(self.drink_maker.execute).to(have_been_called_with('C::'))

    def test_prepare_a_tea_without_sugar_when_tea_is_pressed(self):
        self.coffee_machine.prepare_tea()

        expect(self.drink_maker.execute).to(have_been_called_with('T::'))


    def test_prepare_a_chocolate_without_sugar_when_chocolate_is_pressed(self):
        self.coffee_machine.prepare_chocolate()

        expect(self.drink_maker.execute).to(have_been_called_with('H::'))

    def test_prepare_a_coffee_with_one_sugar_and_stick_when_select_one_sugar_and_coffee_is_pressed(self):
        self.coffee_machine.add_one_sugar()
        self.coffee_machine.prepare_coffee()

        expect(self.drink_maker.execute).to(have_been_called_with('C:1:0'))

    def test_prepare_a_coffee_with_two_sugar_and_stick_when_select_two_sugar_and_coffee_is_pressed(self):
        self.coffee_machine.add_two_sugar()
        self.coffee_machine.prepare_coffee()

        expect(self.drink_maker.execute).to(have_been_called_with('C:2:0'))

    def test_prepare_a_tea_with_one_sugar_and_stick_when_select_one_sugar_and_tea_is_pressed(self):
        self.coffee_machine.add_one_sugar()
        self.coffee_machine.prepare_tea()

        expect(self.drink_maker.execute).to(have_been_called_with('T:1:0'))

    def test_prepare_a_tea_with_two_sugar_and_stick_when_select_one_sugar_and_tea_is_pressed(self):
        self.coffee_machine.add_two_sugar()
        self.coffee_machine.prepare_tea()

        expect(self.drink_maker.execute).to(have_been_called_with('T:2:0'))

    def test_prepare_a_chocolate_with_one_sugar_and_stick_when_select_one_sugar_and_chocolate_is_pressed(self):
        self.coffee_machine.add_one_sugar()
        self.coffee_machine.prepare_chocolate()

        expect(self.drink_maker.execute).to(have_been_called_with('H:1:0'))

    def test_prepare_a_chocolate_with_two_sugar_and_stick_when_select_one_sugar_and_chocolate_is_pressed(self):
        self.coffee_machine.add_two_sugar()
        self.coffee_machine.prepare_chocolate()

        expect(self.drink_maker.execute).to(have_been_called_with('H:2:0'))

    def test_sugar_level_is_not_related_to_previous_drinks(self):
        self.coffee_machine.add_two_sugar()
        self.coffee_machine.prepare_coffee()

        self.coffee_machine.prepare_coffee()

        expect(self.drink_maker.execute).to(have_been_called_with('C::'))

class TestCoffeeMachineGoingIntoBusiness:
    def setup(self):
        self.drink_maker = Spy(CheapDrinkMaker)
        self.adapter = CheapDrinkMakerAdapter(self.drink_maker)
        self.coffee_machine = CoffeeMachine(self.adapter)

    @pytest.mark.parametrize('product,prepare_drink', [
        ('coffee', lambda coffee_machine: coffee_machine.prepare_coffee()),
        ('tea', lambda coffee_machine: coffee_machine.prepare_tea()),
        ('chocolate', lambda coffee_machine: coffee_machine.prepare_chocolate()),
    ])
    def test_drinks_are_not_served_if_no_money_is_added(self, product: str, prepare_drink: callable):
        prepare_drink(self.coffee_machine)

        expect(self.drink_maker.execute).not_to(have_been_called_with('C::'))

    @pytest.mark.parametrize('money', [
        (40),
        (100),
    ])
    def test_coffee_is_prepared_when_there_is_enough_money(self, money: int):
        self.coffee_machine.add_money(money)
        self.coffee_machine.prepare_coffee()

        expect(self.drink_maker.execute).to(have_been_called_with(f'C::'))

    def test_no_message_is_displayed_when_there_is_enough_money(self):
        self.coffee_machine.add_money(100)
        self.coffee_machine.prepare_coffee()

        expect(self.drink_maker.execute).to(have_been_called.once)

    @pytest.mark.parametrize('money,missing_cents', [
        (0, 40),
        (10, 30),
        (39, 1),
    ])
    def test_coffee_shows_the_missing_money_when_there_is_no_enough_money(self, money: int, missing_cents: int):
        self.coffee_machine.add_money(money)
        self.coffee_machine.prepare_coffee()

        expect(self.drink_maker.execute).to(have_been_called_with(f'M:You need to add {missing_cents} cents'))
