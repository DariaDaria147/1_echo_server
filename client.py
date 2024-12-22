# ИСАДИЧЕВА ДАРЬЯ АЛЕКСЕЕВНА, ДПИ22-1

# Код клиента

# Импортируем модуль socket для работы с сетевыми соединениями
import socket
def my_client():
    # Запрашиваем у пользователя хост и порт
    host = input("Введите адрес сервера (по умолчанию 'localhost'): ").strip() or "localhost"
    while True:
        port_input = input("Введите порт сервера (число от 1 до 65535): ").strip()
        if port_input.isdigit() and 1 <= int(port_input) <= 65535:
            port = int(port_input)
            break
        else:
            print("Ошибка: введите корректный номер порта (число от 1 до 65535).")
    print(f"Попытка подключения к серверу {host}:{port}...")

    # Создание сокета
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        try:
            # Подключаемся к серверу
            sock.connect((host, port))
            print(f"Соединение с сервером {host}:{port} установлено - сервер принял подключение.")

            # Цикл, в котором запрашиваются данные
            while True:
                message = input("Введите данные, которые бы хотели отправить серверу: ")
                if not message:
                    print("Сообщение не должно быть пустым. Попробуйте снова, либо напишите 'exit' чтобы разорвать соединение.")
                    continue
                # Если введена команда "exit", разрываем соединение
                if message.strip().lower() == "exit":
                    sock.send(message.encode())
                    break

                # Отправляем данные серверу
                sock.send(message.encode())
                print("Данные были отправлены серверу.")

                # Принимаем данные от сервера порционно
                data = sock.recv(1024)
                print(f"Приём данных от сервера: {data.decode()}")

        # Ошибка подключения
        except ConnectionRefusedError:
            print(f"ОШИБКА! Не удалось подключиться к серверу {host}:{port}. Проверьте сервер, хост и порт.")

        # Прерывание программы
        except KeyboardInterrupt:
            print(f"\nВНИМАНИЕ! Принято KeyboardInterrupt. Принудительный разрыв с сервером.")

    # Закрытие соединения
    print("Разрыв соединения с сервером...")
    sock.close()
    print("Соединение с сервером разорвано.")

if __name__ == "__main__":
    my_client()
