import threading

# Дря работы необходимо создать файл RynnLee.txt
# Блокировка для файла
file_lock = threading.Lock()

# Функция для записи в файл
def write_to_file():
  with file_lock:
    try:
      with open("RynnLee.txt", "a") as file:
        file.write("RynnLee wuz here! Thread: - {}\n".format(threading.get_ident()))
    except Exception as e:
      print(f"Ошибка при записи в файл: {e}")

# Функция для чтения из файла
def read_from_file():
  with file_lock:
    try:
      with open("RynnLee.txt", "r") as file:
        content = file.read()
        print(f"Содержимое прочитанное потоком: {threading.get_ident()}:\n{content}")
    except Exception as e:
      print(f"Ошибка при чтении из файла: {e}")

# Создаем 5 потоков для записи и 5 потоков для чтения
for i in range(5):
  write_thread = threading.Thread(target=write_to_file)
  read_thread = threading.Thread(target=read_from_file)
  write_thread.start()
  read_thread.start()

# Ожидание пока все потоки завершатся
for thread in threading.enumerate():
  if thread != threading.current_thread():
    thread.join()

print("Выполнение завершено - выполнил Долгов Андрей П4Б")
