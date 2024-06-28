from models.admin import Admin
from models.chef import Chef
from models.waiter import Waiter


role_mapping = {
            'Waiter': Waiter,
            'Chef': Chef, 
            'Admin': Admin,
        }