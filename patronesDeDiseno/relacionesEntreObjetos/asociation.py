"""
La asociacion es un tipo de dependencia, en donde
una clase tiene en todo momento acceso o referencia a otra.
"""

class Pet:
    def __init__(self, name: str, age: int, type: str):
        self.__name = name  # encapsulamiento de la var name mediante, __name
        self.__age = age
        self.__type = type
    
    def get_name(self):
        return self.__name
    
    def get_type(self):
        return self.__type
    
    
class Dog(Pet):
    __type = "dog"  # encapsulamiento del atributo de clase.
    
    def __init__(self, name, age, type=__type):
        super().__init__(name, age, type)


class Cat(Pet):
    __type = "cat"
    
    def __init__(self, name, age, type=__type):
        super().__init__(name, age, type)
    
    
class Owner:
    def __init__(self, name: str):
        """Este es un ejemplo de asociacion, no se trata de una relacion de
        dependencia ya que el objeto Pet no se limita al alcance de un metodo;
        mas bien, forman parte del estado interno (contructor) de la clase Owner.
        Si algo falla en la clase Dog, Owner no se podra inicializar.
        """
        self.__name = name
        self.__pet: Pet = Dog("Nala", 3)
        
    def play_with_pet(self):
        return f"{self.__name} is playing with {self.__pet.get_name()}, his {self.__pet.get_type()}."
    
    
if __name__ == "__main__":
    owner = Owner("Jhon")
    print(owner.play_with_pet())