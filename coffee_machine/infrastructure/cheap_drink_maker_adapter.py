from coffee_machine.domain.drink import Drink
from coffee_machine.domain.drink_maker import DrinkMaker
from coffee_machine.domain.drink_type import DrinkType
from coffee_machine.infrastructure.cheap_drink_maker import CheapDrinkMaker


class CheapDrinkMakerAdapter(DrinkMaker):

    def __init__(self, cheap_drink_maker: CheapDrinkMaker) -> None:
        self.cheap_drink_maker = cheap_drink_maker

    def prepare(self, drink: Drink):
        if drink.drink == DrinkType.Coffee:
            if drink.sugar == 0:
                self._prepare_drink('C::')
            elif drink.sugar == 1:
                self._prepare_drink('C:1:0')
            elif drink.sugar == 2:
                self._prepare_drink('C:2:0')
        elif drink.drink == DrinkType.Tea:
            if drink.sugar == 0:
                self._prepare_drink('T::')
            elif drink.sugar == 1:
                self._prepare_drink('T:1:0')
            elif drink.sugar == 2:
                self._prepare_drink('T:2:0')
        else:
            if drink.sugar == 0:
                self._prepare_drink('H::')
            elif drink.sugar == 1:
                self._prepare_drink('H:1:0')
            elif drink.sugar == 2:
                self._prepare_drink('H:2:0')

    def _prepare_drink(self, command):
       self.cheap_drink_maker.execute(command)

