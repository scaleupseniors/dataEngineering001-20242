from pandas import DataFrame, concat

from observer import ObserverInterface


class Sales(ObserverInterface):
    def __init__(self):
        self._users_sales: DataFrame = DataFrame(columns=["user_id", "user_name", "sale_amount"])
        self._products: list[str] = []
    
    
    def add_sale(self, new_sale: DataFrame) -> None:
        self._users_sales = concat([self._users_sales, new_sale], ignore_index=True)
    
    def get_sales(self):
        print(self._users_sales)
    
    def sum_sales(self) -> float:
        return self._users_sales["sale_amount"].sum()
    
    
    def add_product(self, product: str):
        self._products.append(product)
        print(f"A new product: {product} has been added to the sales module!")
    