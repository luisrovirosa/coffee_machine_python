from dataclasses import dataclass

from coffee_machine.domain.drink_type import DrinkType

@dataclass
class Drink:
   type: DrinkType
   sugar: int
   extra_hot: bool