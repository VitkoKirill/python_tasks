from DictDB.database_dict_repository import DatabaseDict
from DictDB.human_model import Human


class HumanService:
    def execute(self, name: str, surname: str, age: int, career: str):
        human = Human(name=name, surname=surname, age=age, career=career)
        db = DatabaseDict()
        key = db.insert(human)
        updated_human = db.get(key)
        updated_human.name = 'name'
        db.update(key=key, value=updated_human)
        db.delete(key)
        print(db.select_all())