# ЗАДАНИЕ 3

import threading

def print_numbers(n):
    for i in range(1, n+1):
        print(i)

def main():
    thread1 = threading.Thread(target=print_numbers, args=(10,))
    thread2 = threading.Thread(target=print_numbers, args=(10,))

    thread1.start()
    thread1.join()

    thread2.start()
    thread2.join()

if __name__ == "__main__":
    main()
