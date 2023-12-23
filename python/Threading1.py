# ЗАДАНИЕ 1
import threading

def calculate_sum(start, end, result):
    s = sum(range(start, end+1))
    result.append(s)

def main():
    N = int(input("Введите N: "))
    result = []

    thread1 = threading.Thread(target=calculate_sum, args=(1, N//3, result))
    thread2 = threading.Thread(target=calculate_sum, args=(N//3 + 1, 2*N//3, result))
    thread3 = threading.Thread(target=calculate_sum, args=(2*N//3 + 1, N, result))

    thread1.start()
    thread2.start()
    thread3.start()

    thread1.join()
    thread2.join()
    thread3.join()

    total_sum = sum(result)
    print(f"Сумма каждого потока: {result}")
    print(f"Общая сумма: {total_sum}")

if __name__ == "__main__":
    main()

