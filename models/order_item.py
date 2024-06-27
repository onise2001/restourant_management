class OrderItem:
    STATUS_CHOICE = (
        "Preparing",
        "Done"
    )

    def __init__(self, dish):
        self.dish = dish
        self.status = self.STATUS_CHOICE[0]
