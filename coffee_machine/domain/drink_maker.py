from abc import ABC, abstractmethod

from coffee_machine.domain.drink import Drink


class DrinkMaker(ABC):
    @abstractmethod
    def prepare(self, drink: Drink) -> None:
        raise NotImplemented()

    @abstractmethod
    def communicate(self, message: str) -> None:
        raise NotImplemented()