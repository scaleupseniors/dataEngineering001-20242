"""
La relacion de dependencia es las mas debil que hay entre clases,
se puede debilitar aun mas mediante el uso de interfaces.
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
        """Este es un ejemplo de dependencia, el objeto Mascota se limita al alcance de un metodo;
        Si los metodos de get_name() o get_type() cambian, el uso de los mismos fallara.
        """
        self.__name = name
        
    def play_with_pet(self, pet: Pet):
        return f"{self.__name} is playing with {pet.get_name()}, his {pet.get_type()}."
    
    
if __name__ == "__main__":
    owner = Owner("Jhon")
    dog = Dog("Nala", 3)
    cat = Cat("Percival", 5)
    print(owner.play_with_pet(cat))