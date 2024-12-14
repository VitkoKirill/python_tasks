import uuid
from uuid import UUID


class DatabaseDict(object):
    dict_db = {}

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(DatabaseDict, cls).__new__(cls)
        return cls.instance

    def insert(self, value: any) -> str:
        key = str(uuid.uuid4())
        if key not in self.dict_db:
            self.dict_db[key] = value
        else:
            raise KeyError(f'Insert: Key {key} already exist!')
        return key

    def get(self, key: str) -> any:
        value = self.dict_db.get(key)
        if value is not None:
            return value
        else:
            raise KeyError(f'Insert: Key {key} does not exist!')

    def update(self, key: str, value: any) -> None:
        if key in self.dict_db:
            self.dict_db[key] = value
        else:
            raise KeyError(f'Update: Key {key} does not exist!')

    def delete(self, key: str) -> None:
        try:
            self.dict_db.pop(key)
        except:
            raise KeyError(f'Delete: Key {key} does not exis!')

    def select_all(self) -> dict:
        return self.dict_db
