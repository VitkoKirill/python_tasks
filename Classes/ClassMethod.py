# Создайте класс Vehicle, содержащий:
# Атрибут класса total_vehicles, отслеживающий количество созданных экземпляров.
# Метод класса create_with_default_engine, который принимает название машины и создает объект с
# предустановленным двигателем (например, "V6").
# Продемонстрируйте использование метода класса и проверьте, что счетчик обновляется корректно.

class Vehicle:
    total_vehicle = 0

    def __init__(self, model, engine, year):
        self.model = model
        self.engine = engine
        self.year = year
        Vehicle.total_vehicle += 1

    @classmethod
    def create_with_default_engine(cls, model, year):
        return cls(model, 'V6', year)

    @staticmethod
    def return_total_vehicle():
        return Vehicle.total_vehicle


car1 = Vehicle('BMW', 'V5', '2021')
car2 = Vehicle('Mercedes', '52', '2024')
print(Vehicle.return_total_vehicle())

car3 = Vehicle.create_with_default_engine('Audi', '2022')
print(Vehicle.return_total_vehicle())
