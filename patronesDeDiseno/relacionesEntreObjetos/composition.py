"""
La composicion es un tipo de agregacion en donde todo el ciclo de vida del
componente es manejado desde la clase quien lo contiene, y por ende,
el componente solo puede existir como parte del contenedor
"""

from typing import Generator

class Pet:
    def __init__(self, name: str, age: int, type: str, action: str):
        self.__name = name  # encapsulamiento de la var name mediante, __name
        self.__age = age
        self.__type = type
        self.action = action
    
    def get_name(self):
        return self.__name
    
    def get_type(self):
        return self.__type
    
    
class Dog(Pet):
    __type = "dog"  # encapsulamiento del atributo de clase.
    __action = "barks"
    
    def __init__(self, name, age, type=__type, action=__action):
        super().__init__(name, age, type, action)


class Cat(Pet):
    __type = "cat"
    __action = "meows"
    
    def __init__(self, name, age, type=__type, action=__action):
        super().__init__(name, age, type, action)

    
class Owner:
    def __init__(self, name: str):
        """
        Este es un ejemplo de composicion, ya que el dueño maneja todo el ciclo de vida
        de los objetos Dog y Cat, desde su creacion hasta su destruccion.
        """
        self.__name = name
        self.__pets: list[Pet] = [Dog("Nala", 3), Cat("Percival", 5)]
    
    def play_with_pets(self):
        for pet in self.__pets:
            print(f"{self.__name} is playing with {pet.get_name()}, his {pet.get_type()} that {pet.action}.")
    
    def get_pets(self) -> Generator:
        for pet in self.__pets: 
            yield pet
        

if __name__ == "__main__":
    owner = Owner("Jhon")
    pets = owner.get_pets()
    owner.play_with_pets()