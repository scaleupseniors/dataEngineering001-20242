from pandas import DataFrame

class Adapter:
    @classmethod
    def adapt_user_sale(cls, user_sale: dict) -> DataFrame:
        return DataFrame(user_sale, index = [0])