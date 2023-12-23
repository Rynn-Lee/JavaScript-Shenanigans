# ЗАДАНИЕ 2

import threading

def print_numbers(n):
    for i in range(1, n+1):
        print(i)

def main():
    N = int(input("Введите N: "))
    threads = []

    for _ in range(3):  # Создаем три потока
        thread = threading.Thread(target=print_numbers, args=(N,))
        threads.append(thread)

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()
