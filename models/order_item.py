
STATUS_CHOICE = (
        "Preparing",
        "Done",
        'Delivered',
)

class OrderItem:
    _id_counter = 0
 
    def __init__(self, dish, order_table, status=STATUS_CHOICE[0], id=None):
        if id is None:
            OrderItem._id_counter += 1
            self.id = OrderItem._id_counter
        else:
            OrderItem._id_counter += 1
            self.id = id

        self.order_table = order_table
        self.dish = dish
        self.status = status or STATUS_CHOICE[0]

