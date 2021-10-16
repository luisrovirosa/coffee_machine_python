from doublex import Spy
from doublex_expects import have_been_called_with
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

    def test_coffee_is_not_served_if_no_money_is_added(self):
        self.coffee_machine.prepare_coffee()

        expect(self.drink_maker.execute).not_to(have_been_called_with('C::'))

    def test_tea_is_not_served_if_no_money_is_added(self):
        self.coffee_machine.prepare_tea()

        expect(self.drink_maker.execute).not_to(have_been_called_with('T::'))

    def test_chocolate_is_not_served_if_no_money_is_added(self):
        self.coffee_machine.prepare_chocolate()

        expect(self.drink_maker.execute).not_to(have_been_called_with('H::'))


