from user import User


class Comment(object):
    def __init__(self, id: str, text: str, rating: float, author: User):
        self.id = id
        self.text = text
        self.rating = rating
        self.author = author
