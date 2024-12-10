from DictDB.database_dict_repository import DatabaseDict
from DictDB.human_model import Human
import uuid

class HumanService:
    def execute(self, name: str, surname: str, age: int, career: str):
        human = Human(name=name, surname=surname, age=age, career=career)
        db = DatabaseDict()
        uid = HumanService.generate_uuid()
        db.insert(uid, human)
        updated_human = db.get(uid)
        updated_human.name = 'name'
        db.update(uid, updated_human)
        db.delete(uid)
        print(db.select_all())

    @staticmethod
    def generate_uuid() -> str:
        return str(uuid.uuid4())