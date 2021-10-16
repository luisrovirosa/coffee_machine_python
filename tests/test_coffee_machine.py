from doublex import Spy
from doublex_expects import have_been_called_with
from expects import expect

from coffee_machine import CoffeeMachine
from coffee_machine.drink_maker import DrinkMaker


class TestCoffeeMachine:

    def test_prepare_a_coffee_without_sugar_when_coffee_is_pressed(self):
        drink_maker = Spy(DrinkMaker)
        coffee_machine = CoffeeMachine(drink_maker)

        coffee_machine.prepare_coffee()

        expect(drink_maker.execute).to(have_been_called_with('C::'))

    def test_prepare_a_tea_without_sugar_when_tea_is_pressed(self):
        drink_maker = Spy(DrinkMaker)
        coffee_machine = CoffeeMachine(drink_maker)

        coffee_machine.prepare_tea()

        expect(drink_maker.execute).to(have_been_called_with('T::'))