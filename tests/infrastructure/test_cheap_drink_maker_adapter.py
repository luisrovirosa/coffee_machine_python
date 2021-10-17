import pytest
from doublex import Spy
from doublex_expects import have_been_called_with
from expects import expect

from coffee_machine.domain.drink import Drink
from coffee_machine.domain.drink_type import DrinkType
from coffee_machine.infrastructure.cheap_drink_maker import CheapDrinkMaker
from coffee_machine.infrastructure.cheap_drink_maker_adapter import CheapDrinkMakerAdapter


class TestCheapDrinkMakerAdapter:
    @pytest.mark.parametrize('drink,expected_command',[
        (Drink(DrinkType.Coffee, 0, False), 'C::'),
        (Drink(DrinkType.Coffee, 1, False), 'C:1:0'),
        (Drink(DrinkType.Coffee, 2, False), 'C:2:0'),
        (Drink(DrinkType.Tea, 0, False), 'T::'),
        (Drink(DrinkType.Tea, 1, False), 'T:1:0'),
        (Drink(DrinkType.Tea, 2, False), 'T:2:0'),
        (Drink(DrinkType.Chocolate, 0, False), 'H::'),
        (Drink(DrinkType.Chocolate, 1, False), 'H:1:0'),
        (Drink(DrinkType.Chocolate, 2, False), 'H:2:0'),
        (Drink(DrinkType.Orange, 0, False), 'O::'),
        (Drink(DrinkType.Orange, 1, False), 'O:1:0'),
        (Drink(DrinkType.Orange, 2, False), 'O:2:0'),
    ])
    def test_adapt_different_types_of_drinks(self, drink: Drink, expected_command: str):
        cheap_drink_maker = Spy(CheapDrinkMaker)
        adapter = CheapDrinkMakerAdapter(cheap_drink_maker)

        adapter.prepare(drink)

        expect(cheap_drink_maker.execute).to(have_been_called_with(expected_command))

    @pytest.mark.parametrize('drink_type,expected_product',[
        (DrinkType.Coffee, 'Ch'),
        (DrinkType.Tea, 'Th'),
        (DrinkType.Chocolate, 'Hh'),
    ])
    def test_can_prepare_extra_hot_drinks(self, drink_type: DrinkType, expected_product: str):
        cheap_drink_maker = Spy(CheapDrinkMaker)
        adapter = CheapDrinkMakerAdapter(cheap_drink_maker)
        drink = Drink(drink_type, 0, True)

        adapter.prepare(drink)

        expect(cheap_drink_maker.execute).to(have_been_called_with(f'{expected_product}::'))


    def test_message_sends_the_command(self):
        cheap_drink_maker = Spy(CheapDrinkMaker)
        adapter = CheapDrinkMakerAdapter(cheap_drink_maker)

        adapter.communicate('hello')

        expect(cheap_drink_maker.execute).to(have_been_called_with('M:hello'))