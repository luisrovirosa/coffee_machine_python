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
      self.drink_maker.execute(command)

   def prepare_tea(self):
      if self.sugar == 0:
         self.drink_maker.execute('T::')
      elif self.sugar == 1:
         self.drink_maker.execute('T:1:0')
      elif self.sugar == 2:
         self.drink_maker.execute('T:2:0')

   def prepare_chocolate(self):
      if self.sugar == 0:
         self.drink_maker.execute('H::')
      elif self.sugar == 1:
         self.drink_maker.execute('H:1:0')
      elif self.sugar == 2:
         self.drink_maker.execute('H:2:0')

   def add_one_sugar(self):
      self.sugar = 1

   def add_two_sugar(self):
      self.sugar = 2