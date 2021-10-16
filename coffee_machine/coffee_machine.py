from coffee_machine.drink_maker import DrinkMaker


class CoffeeMachine:

   def __init__(self, drink_maker: DrinkMaker) -> None:
      self.drink_maker = drink_maker

   def prepare_coffee(self):
      self.drink_maker.execute('C::')
