# Создайте класс Book, содержащий:
# Поля title (название книги) и author (автор).
# Метод __str__, возвращающий строку в формате: "Книга: <название>, Автор: <автор>".
# Создайте несколько объектов и выведите их в консоль, чтобы проверить реализацию.

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f'Book: {self.title}, Author: {self.author}'


book1 = Book('Python', 'Amogus')
book2 = Book('Java', 'Programmer')

print(book1)
print(book2)