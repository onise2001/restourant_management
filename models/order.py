class Order:
    STATUS_CHOICES = (
        "Pending",
        "Preparing",
        "Finished",
    )

    def __init__(self, table, orderitems, waiter):
        self.table = table
        self.orderitems = orderitems
        self.waiter = waiter
        self.status = self.STATUS_CHOICES[0]

    
    

    def order_status(self):
        done_counter = 0
        for order_item in self.orderitems:
            if order_item.status == 'Done':
                done_counter += 0

            else:
                print(f'PREPARING {order_item.dish}')

        if done_counter == len(self.orderitems):
            self.status = self.STATUS_CHOICES[2]
            print("ORDER PREPARED")
            

