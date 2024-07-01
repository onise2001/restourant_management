ROLE_CHOICES = (
    "Admin",
    "Chef",
    "Accoutant",
    "Waiter",
    "Warehouse Worker",
)



class User:

    def __init__(self, username, password, email, role):
        self.username = username
        self.password = password
        self.email = email
        self.role = role
        


    @property
    def role(self):
        return self._role

    
    @role.setter
    def role(self, role):
        if role in ROLE_CHOICES:
            self._role = role
            return role
        raise ValueError("No such role")