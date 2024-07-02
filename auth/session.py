from models.user import User
#from .permissions import role_mapping
from models.restourant import Restourant
from models.admin import Admin
from models.chef import Chef
from models.waiter import Waiter
from models.worker import WarehouseWorker
from models.accoutant import Accoutant


def singleton(cls):
    instances = {}
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return get_instance

@singleton
class Session:
    def __init__(self):
        self._current_user = None
        self.restourant = Restourant()
        self.role_mapping = {
            'Waiter': Waiter,
            'Chef': Chef, 
            'Admin': Admin,
            'Worker': WarehouseWorker,
            'Accoutant': Accoutant,
        }
        


    @property
    def current_user(self):
        return self._current_user
    
    @current_user.setter
    def current_user(self, user):
        if isinstance(user, User):
            role_class = self.role_mapping.get(user.role)
            if role_class:
                self._current_user = role_class(user)
            return user
        raise ValueError('Please provide User object')
    

