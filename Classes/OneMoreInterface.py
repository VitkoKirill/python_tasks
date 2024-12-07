# Создайте интерфейс PaymentProcessor, в котором:
# Метод process_payment(amount: float) -> None.
# Создайте классы:
# CardPaymentProcessor, который имитирует обработку платежа банковской картой.
# CryptoPaymentProcessor, который имитирует обработку платежа в криптовалюте.
# Для каждого класса реализуйте метод process_payment с выводом уникальных сообщений.
# Продемонстрируйте использование обоих классов через цикл, где у каждого будет вызываться process_payment с разной суммой.


from abc import ABC, abstractmethod


class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount: float) -> None:
        pass


class CardPaymentProcessor(PaymentProcessor):
    def process_payment(self, amount: float) -> None:
        print(f'Processing card payment, amount: {amount}')


class CryptoPaymentProcessor(PaymentProcessor):
    def process_payment(self, amount: float) -> None:
        print(f'Processing crypto payment, amount: {amount}')

card_payment_processor = CardPaymentProcessor()
card_payment_processor.process_payment(100.25)

crypto_payment_processor = CryptoPaymentProcessor()
crypto_payment_processor.process_payment(500.55)