from DictDB.database_dict_repository import DatabaseDict
import uuid


class Repository:
    db = DatabaseDict()

    def retrieve(self, key: uuid) -> any:
        return self.db.get(key)

    def post(self, value: any) -> uuid.UUID:
        return self.db.insert(value)

    def remove(self, key: uuid):
        self.db.delete(key)

    def update(self, key: uuid, value: any) -> None:
        return self.db.update(key=key, value=value)

    def show_all(self):
        print(self.db.select_all())
