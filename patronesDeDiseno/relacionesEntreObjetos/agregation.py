"""
La agregacion es un tipo de asociacion, en donde un objeto sirve como
coleccion de un grupo de objetos.
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
    def __init__(self):
        self.__pets: list[Pet] = []  # Agregacion, el dueño tiene mascotas
        
    def adopt_pets(self, pets: list[Pet]):
        self.__pets += pets  # Las mascotas son agregadas al dueño