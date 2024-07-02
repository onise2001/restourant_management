import csv
from paths import ORDER_PATH
from update_func import update_value_in_csv


STATUS_CHOICES = (
    "Pending",
    "Preparing",
    "Finished",
)

PAYMENT_CHOICES = (
    'Paid',
    'Unpaid'
)

class Order:
    def __init__(self, table, orderitems, waiter, status=STATUS_CHOICES[0], payement=PAYMENT_CHOICES[1]):
        self.table = table
        self.orderitems = orderitems
        self.waiter = waiter
        self.status = status
        self.payement = payement

    def order_status(self):
        done_counter = 0
        from auth.create_session import session

        print(f'Table {self.table} order items.')

        for order_item in self.orderitems:
            print(f'id: {order_item.id} dish - {order_item.dish}, status: {order_item.status}')
            if order_item.status == 'Done' or 'Delivered':
                done_counter += 1

        if done_counter == len(self.orderitems):
            self.status = STATUS_CHOICES[2]
            update_value_in_csv(
                value=STATUS_CHOICES[2], 
                identifier=self.table, 
                path=ORDER_PATH, 
                identifier_column='table', 
                value_column='status')

            session.restourant.kitchen.current_orders.remove(self)

        print(f'Order Status: {self.status}')
        return 

        

        


