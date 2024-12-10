class DatabaseDict(object):
    dict_db = {}

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(DatabaseDict, cls).__new__(cls)
        return cls.instance

    def insert(self, key: str, value: any) -> None:
        if key not in self.dict_db:
            self.dict_db[key] = value
        else:
            print(f'Insert: Key {key} already exists!')

    def get(self, key: str) -> any:
        return self.dict_db.get(key)

    def update(self, key: str, value: any) -> None:
        if key in self.dict_db:
            self.dict_db[key] = value
        else:
            print(f'Update: Key {key} does not exist!')

    def delete(self, key: str) -> None:
        try:
            self.dict_db.pop(key)
        except KeyError:
            print(f'Delete: Key {key} does not exist!')

    def select_all(self) -> dict:
        return self.dict_db