from coffee_machine.domain.drink import Drink
from coffee_machine.infrastructure.cheap_drink_maker import CheapDrinkMaker


class CoffeeMachine:
   def __init__(self, drink_maker: CheapDrinkMaker) -> None:
      self.drink_maker = drink_maker
      self.current_drink = Drink()

   def prepare_coffee(self):
      if self.current_drink.sugar == 0:
         command = 'C::'
      elif self.current_drink.sugar == 1:
         command = 'C:1:0'
      elif self.current_drink.sugar == 2:
         command = 'C:2:0'
      self._prepare_drink(command)

   def prepare_tea(self):
      if self.current_drink.sugar == 0:
         self._prepare_drink('T::')
      elif self.current_drink.sugar == 1:
         self._prepare_drink('T:1:0')
      elif self.current_drink.sugar == 2:
         self._prepare_drink('T:2:0')

   def prepare_chocolate(self):
      if self.current_drink.sugar == 0:
         self._prepare_drink('H::')
      elif self.current_drink.sugar == 1:
         self._prepare_drink('H:1:0')
      elif self.current_drink.sugar == 2:
         self._prepare_drink('H:2:0')

   def add_one_sugar(self):
      self.current_drink.sugar = 1

   def add_two_sugar(self):
      self.current_drink.sugar = 2

   def _prepare_drink(self, command):
      self.drink_maker.execute(command)
      self.current_drink.sugar = 0