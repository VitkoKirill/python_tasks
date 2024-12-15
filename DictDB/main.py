from DictDB.human_service import HumanService

human_service = HumanService()

key = human_service.post('Mike', 'Nike', 52, 'Programmer')
updated_human = human_service.retrieve(key)
updated_human.age = 45
human_service.update(key=key, value=updated_human)
human_service.remove(key)
human_service.show_all()
