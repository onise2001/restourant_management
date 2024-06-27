class Order:
    STATUS_CHOICES = (
        "Not Finished",
        "Finished",
    )

    def __init__(self,table, dishes, waiter):
        self.table = table
        self.dishes = dishes
        self.waiter = waiter
        self.status = self.STATUS_CHOICES[0]