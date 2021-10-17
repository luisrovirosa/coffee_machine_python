from dataclasses import dataclass

from coffee_machine.domain.drink_type import DrinkType

@dataclass
class Drink:
   type: DrinkType
   sugar: int
   extra_hot: bool
   def __init__(self, type: DrinkType, sugar: int, extra_hot: bool) -> None:
      self.type = type
      self.sugar = sugar
      self.extra_hot = extra_hot if type is not DrinkType.Orange else False

