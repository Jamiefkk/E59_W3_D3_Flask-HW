class Order:
    def __init__(self, customer_name, order_date, quantity):
        self._customer_name = customer_name
        self._order_date = order_date
        self._quantity = quantity