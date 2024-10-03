import threading
import random
import time


class Bank:
    def __init__(self):
        self.balance = 0  # начальный баланс
        self.lock = threading.Lock()  # объект блокировки

    def deposit(self):
        for _ in range(100):
            amount = random.randint(50, 500)  # случайное число для пополнения
            self.lock.acquire()  # вручную захватываем блокировку
            try:
                self.balance += amount
                print(f"Пополнение: {amount}. Баланс: {self.balance}")
            finally:
                self.lock.release()  # освобождаем блокировку в блоке finally
            time.sleep(0.001)  # имитация времени выполнения

    def take(self):
        for _ in range(100):
            amount = random.randint(50, 500)  # случайное число для снятия
            print(f"Запрос на {amount}")
            self.lock.acquire()  # вручную захватываем блокировку
            try:
                if amount <= self.balance:
                    self.balance -= amount
                    print(f"Снятие: {amount}. Баланс: {self.balance}")
                else:
                    print("Запрос отклонён, недостаточно средств")
            finally:
                self.lock.release()  # освобождаем блокировку в блоке finally
            time.sleep(0.001)  # имитация времени выполнения


# Создаем объект класса Bank
bk = Bank()

# Создаем два потока для методов deposit и take
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

# Запускаем потоки
th1.start()
th2.start()

# Ожидаем завершения потоков
th1.join()
th2.join()

# Выводим итоговый баланс
print(f'Итоговый баланс: {bk.balance}')
