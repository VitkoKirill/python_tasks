# Создайте класс MathOperations, в котором будет:
# Статический метод is_even, принимающий целое число и возвращающий True,
# если оно четное, и False в противном случае.
# Статический метод factorial, который возвращает факториал числа.
# Напишите код, который вызывает эти методы без создания экземпляра класса.

class MathOperations:
    @staticmethod
    def is_even(n: int) -> bool:
        return n % 2 == 0

    @staticmethod
    def factorial(n: int) -> int:
        if n == 0:
            return 1
        else:
            return n * MathOperations.factorial(n - 1)


print(MathOperations.is_even(5))
print(MathOperations.is_even(4))
print(MathOperations.factorial(5))
print(MathOperations.factorial(0))
