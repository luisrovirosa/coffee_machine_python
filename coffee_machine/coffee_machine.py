from coffee_machine.drink_maker import DrinkMaker


class CoffeeMachine:
   def __init__(self, drink_maker: DrinkMaker) -> None:
      self.drink_maker = drink_maker
      self.sugar = 0

   def prepare_coffee(self):
      if self.sugar != 1:
         self.drink_maker.execute('C::')
      else:
         self.drink_maker.execute('C:1:0')

   def prepare_tea(self):
      self.drink_maker.execute('T::')

   def prepare_chocolate(self):
      self.drink_maker.execute('H::')

   def add_one_sugar(self):
      self.sugar = 1