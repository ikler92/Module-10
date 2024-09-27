import time
from time import sleep
import threading


# Функция записи слов в файл
def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as f:
        for i in range(1, word_count + 1):
            f.write(f"Какое-то слово № {i}\n")
            sleep(0.1)
    print(f"Завершилась запись в файл {file_name}")


# Замер времени выполнения последовательного вызова функций
start_time = time.time()

# Вызов функции write_words с аргументами
write_words(10, "example1.txt")
write_words(30, "example2.txt")
write_words(200, "example3.txt")
write_words(100, "example4.txt")

end_time = time.time()
print(f"Работа функций заняла {end_time - start_time}")

# Замер времени выполнения потоков
start_time_threads = time.time()

# Создание потоков для параллельного выполнения
threads = [
    threading.Thread(target=write_words, args=(10, "example5.txt")),
    threading.Thread(target=write_words, args=(30, "example6.txt")),
    threading.Thread(target=write_words, args=(200, "example7.txt")),
    threading.Thread(target=write_words, args=(100, "example8.txt")),
]

# Запуск потоков
for thread in threads:
    thread.start()

# Ожидание завершения всех потоков
for thread in threads:
    thread.join()

end_time_threads = time.time()
print(f"Работа потоков заняла {end_time_threads - start_time_threads}")
