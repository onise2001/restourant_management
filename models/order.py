import csv
from paths import ORDER_PATH
from update_func import update_value_in_csv


STATUS_CHOICES = (
    "Pending",
    "Preparing",
    "Finished",
)
class Order:

    def __init__(self, table, orderitems, waiter, status=STATUS_CHOICES[0]):
        self.table = table
        self.orderitems = orderitems
        self.waiter = waiter
        self.status = status

    
    

    def order_status(self):
        done_counter = 0
        print(self.table, self.status)

        for order_item in self.orderitems:
            print(f'id: {order_item.id} dish - {order_item.dish}, status: {order_item.status}')
            if order_item.status == 'Done':
                done_counter += 1

        if done_counter == len(self.orderitems):
            self.status = STATUS_CHOICES[2]
            update_value_in_csv(value=STATUS_CHOICES[2], identifier=self.table, path=ORDER_PATH, identifier_column='table', value_column='status')


        return 

        

        


