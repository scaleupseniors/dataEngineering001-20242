from observer import ObserverInterface

class Marketing(ObserverInterface):
    def __init__(self):
        self._products = []
                
    def add_product(self, product:str):
        self._products.append(product)
        print(f"The new product: {product} has been added to the marketing module!")