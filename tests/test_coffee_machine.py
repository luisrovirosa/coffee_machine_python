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

    def prepare_coffee(coffee_machine: CoffeeMachine):
        return coffee_machine.prepare_coffee()

    def prepare_tea(coffee_machine: CoffeeMachine):
        return coffee_machine.prepare_tea()

    def prepare_chocolate(coffee_machine: CoffeeMachine):
        return coffee_machine.prepare_chocolate()

    @pytest.mark.parametrize('prepare_drink', [
        (prepare_coffee),
        (prepare_tea),
        (prepare_chocolate),
    ])
    def test_drinks_are_not_served_if_no_money_is_added(self, prepare_drink: callable):
        prepare_drink(self.coffee_machine)

        expect(self.drink_maker.execute).not_to(have_been_called_with('C::'))

    @pytest.mark.parametrize('prepare_drink,money', [
        (prepare_coffee, 60),
        # (prepare_tea, 40),
        # (prepare_chocolate, 50),
        (prepare_coffee, 100),
        (prepare_tea, 100),
        (prepare_chocolate, 100),
    ])
    def test_drinks_are_prepared_when_there_is_enough_money(self, prepare_drink: callable, money: int):
        self.coffee_machine.add_money(money)
        self.coffee_machine.prepare_coffee()

        expect(self.drink_maker.execute).to(have_been_called_with(f'C::'))

    @pytest.mark.parametrize('prepare_drink', [
        (prepare_coffee),
        (prepare_tea),
        (prepare_chocolate),
    ])
    def test_no_message_is_displayed_when_there_is_enough_money(self, prepare_drink: callable):
        self.coffee_machine.add_money(100)
        prepare_drink(self.coffee_machine)

        expect(self.drink_maker.execute).to(have_been_called.once)

    @pytest.mark.parametrize('prepare_drink,money,missing_cents', [
        (prepare_coffee, 0, 60),
        (prepare_coffee, 10, 50),
        (prepare_coffee, 59, 1),
    ])
    def test_shows_the_missing_money_when_there_is_no_enough_money(self, prepare_drink: callable, money: int, missing_cents: int):
        self.coffee_machine.add_money(money)
        prepare_drink(self.coffee_machine)

        expect(self.drink_maker.execute).to(have_been_called_with(f'M:You need to add {missing_cents} cents'))
