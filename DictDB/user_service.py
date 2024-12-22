import uuid
import datetime
from uuid import UUID
from DictDB.repository import Repository
from DictDB.user_model import User


class UserService:

    def __init__(self):
        self.repository = Repository()

    def get(self, key: uuid) -> User:
        return self.repository.retrieve(key)

    def post(self, name: str, surname: str, age: int, career: str) -> UUID:
        user = User(name=name, surname=surname, age=age, career=career)
        user.created_at = datetime.datetime.now()
        return self.repository.post(user)

    def remove(self, key: uuid):
        self.repository.remove(key)

    def update(self, key: uuid, user: User) -> None:
        user.updated_at = datetime.datetime.now()
        return self.repository.update(key, user)

    def show_all(self):
        self.repository.show_all()
