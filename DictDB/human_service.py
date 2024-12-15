import uuid
from uuid import UUID
from DictDB.database_dict_repository import DatabaseDict
from DictDB.human_model import Human


class HumanService:
    db = DatabaseDict()

    def retrieve(self, key: uuid) -> Human:
        return self.db.get(key)

    def post(self, name: str, surname: str, age: int, career: str) -> UUID:
        return self.db.insert(Human(name=name, surname=surname, age=age, career=career))

    def remove(self, key: uuid):
        self.db.delete(key)

    def update(self, key: uuid, value: Human) -> None:
        return self.db.update(key=key, value=value)

    def show_all(self):
        print(self.db.select_all())
