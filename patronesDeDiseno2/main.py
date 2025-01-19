from user import User
from sales import Sales
from adapter import Adapter
from marketing import Marketing
from memento import Memento

u1, u2 = User("Santiago"), User("Samuel")
sales = Sales()
marketing = Marketing()

for _ in range(4):
    sales.add_sale(Adapter.adapt_user_sale(u1.generate_sale()))
    sales.add_sale(Adapter.adapt_user_sale(u2.generate_sale()))

sales.get_sales()

print(Memento.get_previous_user_sale("Santiago"))
print(Memento.get_previous_user_sale("Samuel"))