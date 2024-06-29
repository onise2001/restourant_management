import os
from pathlib import Path

# Define the relative path to the CSV file


current_dir = os.path.dirname(os.path.abspath(__file__))
base_dir = os.path.abspath(current_dir)


USERS_PATH = Path(f'{base_dir}/restourant/users.csv')
TABLES_PATH = Path(f'{base_dir}/restourant/tables.csv')
KITCHEN_PATH = Path(f'{base_dir}/restourant/kitchen.csv')
DISH_PATH = Path(f'{base_dir}/restourant/dishes.csv')
ORDER_PATH = Path(f'{base_dir}/restourant/orders.csv')
ORDER_ITEM_PATH = Path(f'{base_dir}/restourant/orders-items.csv')

WAREHOUSER_PATH = Path(f'{base_dir}/restourant/warehouse.csv')



