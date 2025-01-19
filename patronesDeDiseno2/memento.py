class Memento:
    history = {}
     
    @classmethod
    def save_user_sales(cls, username: str, sale: int) -> None:
        if cls.history.get(username) is None:
            cls.history[username] = [sale]
        cls.history[username].append(sale)
        
    @classmethod
    def get_previous_user_sale(cls, username: str) -> float:
        try:
            return cls.history[username][-2]  # -1 should be the actual sale
        except (KeyError, IndexError):
            return None