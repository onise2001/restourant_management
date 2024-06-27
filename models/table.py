class Table:

    STATUS_CHOICES = (
        "Unoccupied",
        "Occupied",
    )

    def __init__(self, number):
        self.number = number
        self.status = self.STATUS_CHOICES[0]