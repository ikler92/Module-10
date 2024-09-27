import os
import time
from multiprocessing import Pool


# Функция для чтения информации из файла
def read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf-8') as file:
        while True:
            line = file.readline()
            if not line:
                break
            all_data.append(line)


# Список названий файлов
filenames = [f'./file {number}.txt' for number in range(1, 5)]  # Предполагаем, что файлы называются file_1.txt и т.д.


# Линейный вызов
def linear_reading():
    start_time = time.time()
    for filename in filenames:
        read_info(filename)
    end_time = time.time()
    print(f"Линейный вызов занял: {end_time - start_time} секунд")


# Многопроцессный вызов
def multiprocess_reading():
    start_time = time.time()
    with Pool() as pool:
        pool.map(read_info, filenames)
    end_time = time.time()
    print(f"Многопроцессный вызов занял: {end_time - start_time} секунд")


if __name__ == '__main__':
    # Линейный вызов
    linear_reading()

    # Многопроцессный вызов
    multiprocess_reading()
