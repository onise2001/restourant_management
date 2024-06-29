from models.admin import Admin
from models.chef import Chef
from models.waiter import Waiter
from models.worker import WarehouseWorker


role_mapping = {
    'Waiter': Waiter,
    'Chef': Chef, 
    'Admin': Admin,
    'Worker': WarehouseWorker,
}