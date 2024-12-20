"""
Singleton se usa cuando necesito asegurarme de que solo exista una instancia de clase
en toda la aplicacion. Aqui va a existir una unica instancia de informacion
de orden para toda la aplicacion. 
"""

class OrderInfo:
    def __init__(self, info: dict):
        self.info = info

class Singleton:
    info_orden = None  #static
    
    @classmethod
    def get_info_orden(cls):
        if cls.info_orden is None:
            cls.info_orden = OrderInfo({})
        return cls.info_orden
        
    
class Order:
    info_orden: dict = Singleton.get_info_orden()
    
    @classmethod
    def check_order(cls):
        assert cls.info_orden.info.get("order_number") is not None
        assert cls.info_orden.info.get("payment") is not None
        assert cls.info_orden.info["payment"] == True
    
         
class Customer:
    info_orden: dict = Singleton.get_info_orden()
    
    @classmethod
    def place_order(cls):
        cls.info_orden.info["order_number"] = 125720
        return cls
        
    @classmethod
    def pay_order(cls):
        cls.info_orden.info["payment"] = True
        return cls
        

if __name__ == "__main__":
    person = Customer.place_order()
    order = Order.check_order()  # va a fallar por que el cliente no ha pagado la orden.