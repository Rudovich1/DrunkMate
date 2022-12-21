import enum


class Role(enum.Enum):
    USER = 0
    DRUNKMASTER = 1


class User(object):
    def __init__(self,
                 id: str,
                 login: str,
                 hashed_password: str,
                 name: str,
                 role: Role):
        self.id = id
        self.login = login
        self.hashed_password = hashed_password
        self.name = name
        self.role = role
