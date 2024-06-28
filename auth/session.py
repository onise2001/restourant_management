from models.user import User


class Session:
    def __init__(self):
        self._current_user = None


    @property
    def current_user(self):
        return self._current_user
    
    @current_user.setter
    def current_user(self, user):
        if isinstance(user, User):
            self._current_user = user
            return user
        raise ValueError('Please provide User object')