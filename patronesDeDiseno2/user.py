from random import randint

from observer import ObserverInterface
from memento import Memento

class User:  # subject
    def __init__(self, name: str):
        self._name = name
        self._id = randint(1,200)
        self._observers: list[ObserverInterface] = []
        self._previous_sale: None | float = Memento.get_previous_user_sale(self._name)
        
        
    def generate_sale(self) -> dict:
        new_sale =  {
            "user_id": self._id, 
            "user_name": self._name, 
            "sale_amount": randint(1,1000)
        }
        Memento.save_user_sales(self._name,  new_sale["sale_amount"])
        self._previous_sale = Memento.get_previous_user_sale(self._name)
        return new_sale
        
        
    def add_observer(self, module: ObserverInterface) -> None:
        self._observers.append(module)
    
    
    def add_product(self, product: str):
        # Let's notify all observers that a new product has been created by the user.
        for observer in self._observers:
            observer.add_product(product)
        
            
    def __str__(self):
        return f"user_id: {self._id}, user_name: {self._name}, observers: {self._observers}"
    