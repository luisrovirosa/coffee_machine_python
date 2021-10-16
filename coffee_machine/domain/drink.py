from dataclasses import dataclass

from coffee_machine.domain.drink_type import DrinkType

@dataclass
class Drink:
   drink: DrinkType = DrinkType.Coffee
   sugar: int = 0