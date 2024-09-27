import threading
import time


# Класс Knight, наследованный от Thread
class Knight(threading.Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power

    # Метод run, который будет выполняться в потоке
    def run(self):
        print(f"{self.name}, на нас напали!")
        enemies = 100  # У всех рыцарей 100 врагов
        days = 0  # Считаем дни
        while enemies > 0:
            days += 1
            time.sleep(1)  # Один день сражения равен одной секунде
            enemies -= self.power
            enemies = max(enemies, 0)  # Убедимся, что количество врагов не станет отрицательным
            print(f"{self.name} сражается {days} день(дня)..., осталось {enemies} воинов.")

        print(f"{self.name} одержал победу спустя {days} дней(дня)!")


# Создаем двух рыцарей
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

# Запуск потоков
first_knight.start()
second_knight.start()

# Ожидание завершения потоков
first_knight.join()
second_knight.join()

# Вывод строки об окончании сражений
print("Все битвы закончились!")
