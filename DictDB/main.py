import time

from DictDB.user_service import UserService

user_service = UserService()

key = user_service.post('Mike', 'Nike', 52, 'Programmer')
updated_user = user_service.get(key)
print(updated_user.__dict__)
updated_user.age = 45
time.sleep(2)
user_service.update(key=key, user=updated_user)
print(updated_user.__dict__)
user_service.remove(key)
user_service.show_all()
