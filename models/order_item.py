
STATUS_CHOICE = (
        "Preparing",
        "Done"
)

class OrderItem:
    _id_counter = 0
 

    def __init__(self, dish, order_table, status=STATUS_CHOICE[0]):
        OrderItem._id_counter += 1
        self.id = OrderItem._id_counter
        self.order_table = order_table
        self.dish = dish
        self.status = status

