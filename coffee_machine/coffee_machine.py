from coffee_machine.drink_maker import DrinkMaker


class CoffeeMachine:
   def __init__(self, drink_maker: DrinkMaker) -> None:
      self.drink_maker = drink_maker
      self.sugar = 0

   def prepare_coffee(self):
      if self.sugar == 0:
         command = 'C::'
      elif self.sugar == 1:
         command = 'C:1:0'
      elif self.sugar == 2:
         command = 'C:2:0'
      self._prepare_drink(command)

   def prepare_tea(self):
      if self.sugar == 0:
         self._prepare_drink('T::')
      elif self.sugar == 1:
         self._prepare_drink('T:1:0')
      elif self.sugar == 2:
         self._prepare_drink('T:2:0')

   def prepare_chocolate(self):
      if self.sugar == 0:
         self._prepare_drink('H::')
      elif self.sugar == 1:
         self._prepare_drink('H:1:0')
      elif self.sugar == 2:
         self._prepare_drink('H:2:0')

   def add_one_sugar(self):
      self.sugar = 1

   def add_two_sugar(self):
      self.sugar = 2

   def _prepare_drink(self, command):
      self.drink_maker.execute(command)