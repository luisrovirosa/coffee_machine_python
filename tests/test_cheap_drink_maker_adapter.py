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
        (Drink(DrinkType.Coffee, 0), 'C::'),
        (Drink(DrinkType.Coffee, 1), 'C:1:0'),
        (Drink(DrinkType.Coffee, 2), 'C:2:0'),
        (Drink(DrinkType.Tea, 0), 'T::'),
        (Drink(DrinkType.Tea, 1), 'T:1:0'),
        (Drink(DrinkType.Tea, 2), 'T:2:0'),
        (Drink(DrinkType.Chocolate, 0), 'H::'),
        (Drink(DrinkType.Chocolate, 1), 'H:1:0'),
        (Drink(DrinkType.Chocolate, 2), 'H:2:0'),
    ])
    def test_adapt_different_types_of_drinks(self, drink: Drink, expected_command: str):
        cheap_drink_maker = Spy(CheapDrinkMaker)
        adapter = CheapDrinkMakerAdapter(cheap_drink_maker)

        adapter.prepare(drink)

        expect(cheap_drink_maker.execute).to(have_been_called_with(expected_command))
