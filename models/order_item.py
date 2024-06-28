class OrderItem:
    _id_counter = 0
    STATUS_CHOICE = (
        "Preparing",
        "Done"
    )

    def __init__(self, dish, order):
        OrderItem._id_counter += 1
        self.id = OrderItem._id_counter
        self.order = order
        self.dish = dish
        self.status = self.STATUS_CHOICE[0]


    