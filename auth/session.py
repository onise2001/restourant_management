from models.kitchen import Kitchen
from models.warehouse import Warehouse
from models.user import User
from .permissions import role_mapping

class Session:
    def __init__(self):
        self._current_user = None
        self.kitchen = Kitchen()
        self.warehouse = Warehouse()
    


    @property
    def current_user(self):
        return self._current_user
    
    @current_user.setter
    def current_user(self, user):
        if isinstance(user, User):
            role_class = role_mapping.get(user.role)
            if role_class:
                self._current_user = role_class(user)
            return user
        
        elif user is None:
            self._current_user = None
            
        raise ValueError('Please provide User object')
    


        