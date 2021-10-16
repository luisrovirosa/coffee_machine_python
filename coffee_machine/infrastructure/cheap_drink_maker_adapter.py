from coffee_machine.domain.drink import Drink
from coffee_machine.domain.drink_maker import DrinkMaker
from coffee_machine.domain.drink_type import DrinkType
from coffee_machine.infrastructure.cheap_drink_maker import CheapDrinkMaker


class CheapDrinkMakerAdapter(DrinkMaker):

    def __init__(self, cheap_drink_maker: CheapDrinkMaker) -> None:
        self.cheap_drink_maker = cheap_drink_maker

    def prepare(self, drink: Drink):
        if drink.sugar == 0:
            self._prepare_drink(f"{self._drink(drink)}:{self._sugar(drink)}:{self._stick(drink)}")
        elif drink.sugar == 1:
            self._prepare_drink(f"{self._drink(drink)}:{self._sugar(drink)}:{self._stick(drink)}")
        elif drink.sugar == 2:
            self._prepare_drink(f"{self._drink(drink)}:{self._sugar(drink)}:{self._stick(drink)}")

    def _prepare_drink(self, command):
       self.cheap_drink_maker.execute(command)

    @staticmethod
    def _drink(drink: Drink):
        drink_codes = {
            DrinkType.Coffee: 'C',
            DrinkType.Tea: 'T',
            DrinkType.Chocolate: 'H',
        }
        return drink_codes[drink.drink]

    @staticmethod
    def _sugar(drink: Drink):
        if drink.sugar == 0:
            return ''
        else:
            return drink.sugar

    @staticmethod
    def _stick(drink: Drink):
        if drink.sugar != 0:
            return '0'
        else:
            return ''

