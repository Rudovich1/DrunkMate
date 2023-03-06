import enum


class Role(enum.Enum):
    USER = 0
    DRUNKMASTER = 1


class User(object):
    def __init__(self, id: str, login: str, name: str, role: Role):
        self.id = id
        self.login = login
        self.name = name
        self.role = role
