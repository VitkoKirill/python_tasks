# Создайте интерфейс Logger, который содержит:
# Метод log_info(message: str) -> None.
# Метод log_error(message: str) -> None.
# Создайте два класса, реализующих этот интерфейс:
# FileLogger, который записывает сообщения в файл log.txt.
# ConsoleLogger, который выводит сообщения в консоль.
# Дополнительно:
# Создайте интерфейс AdvancedLogger, который наследуется от Logger и добавляет метод log_warning(message: str) -> None.
# Создайте класс AdvancedFileLogger, который реализует этот интерфейс и дополняет поведение логирования.
# Напишите пример использования для обоих интерфейсов.
from abc import ABC, abstractmethod


class Logger(ABC):
    @abstractmethod
    def log_info(self, message: str) -> None:
        pass

    @abstractmethod
    def log_error(self, message: str) -> None:
        pass


class AdvancedLogger(Logger):
    @abstractmethod
    def log_warning(self, message: str) -> None:
        pass


class FileLogger(Logger):
    def log_info(self, message: str) -> None:
        with open('log.txt', 'a') as f:
            f.write('Info: ' + message + '\n')

    def log_error(self, message: str) -> None:
        with open('log.txt', 'a') as f:
            f.write('Error: ' + message + '\n')


class ConsoleLogger(Logger):
    def log_info(self, message: str) -> None:
        print('Info: ' + message)

    def log_error(self, message: str) -> None:
        print('Error: ' + message)

class AdvancedFileLogger(AdvancedLogger):
    def log_info(self, message: str) -> None:
        with open('log.txt', 'a') as f:
            f.write('AdvancedFileLogger Info: ' + message + '\n')

    def log_error(self, message: str) -> None:
        with open('log.txt', 'a') as f:
            f.write('AdvancedFileLogger Error: ' + message + '\n')

    def log_warning(self, message: str) -> None:
        with open('log.txt', 'a') as f:
            f.write('AdvancedFileLogger Warning: ' + message + '\n')


file_logger = FileLogger()
file_logger.log_info('Hello')
file_logger.log_error('Mistake!')

console_logger = ConsoleLogger()
console_logger.log_info('Hi')
console_logger.log_error('Something went wrong!')

advanced_file_logger = AdvancedFileLogger()
advanced_file_logger.log_info('Hello')
advanced_file_logger.log_error('Mistake!')
advanced_file_logger.log_warning('Something went wrong!')
