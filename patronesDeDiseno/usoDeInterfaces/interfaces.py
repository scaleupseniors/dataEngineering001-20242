"""
En python no hay interfaces, interfaces. Existen clases abstractas que se comportan
muy parecido a una interfaz
"""

from abc import ABC, abstractmethod

class PetInterface(ABC):  # importamos de abstract base class
    def __init__(self, name: str, type: str):
        self.__name = name
        self.__type = type
        
    def eat(self):
        """
        En las interfaces todos los metodos no deben de poseer implementacion,
        y todos las clases que las implementen deben de establecer el funcionamiento
        de los metodos. En las clases abstractas no es asi, solo los metodos que tengan
        el decorador @abstractmethod deben de ser implementados por las clases que heredan,
        ademas, los metodos pueden tener implementaciones concretas.
        
        TANTO LAS INTERFACES COMO LAS CLASES ABSTRACTAS NO PUEDEN SER INSTANCIADAS.
        """
        return f"{self.__name} is eating."
    
    @abstractmethod
    def sleep(self):
        pass
    

class Cat(PetInterface):
    __type: str = "cat"
    def __init__(self, name, type=__type):
        super().__init__(name, type)
        
    # @override
    def sleep(self):
        print("Cats tend to sleep between 12 - 16 hours per day.")
  
    
class Dog(PetInterface):
    __type: str = "dog"
    def __init__(self, name, type=__type):
        super().__init__(name, type)
    
    # @override
    def sleep(self):
        print("Dogs tend to sleep between 8 - 13 hours per day.")
    
        
        