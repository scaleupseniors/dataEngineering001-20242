from abc import ABC, abstractmethod


class ObserverInterface(ABC):
    @abstractmethod
    def add_product(self, product: str) -> None:
        ...