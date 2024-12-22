# ИСАДИЧЕВА ДАРЬЯ АЛЕКСЕЕВНА, ДПИ22-1

# Код сервера

# Импортируем модуль socket для работы с сетевыми соединениями
import socket

def my_server():
    # Устанавливаем хост (пустая строка) и порт (0-65535)
    host = ''

    # Запрашиваем порт у пользователя
    while True:
        port_input = input("Введите порт для запуска сервера (число от 1 до 65535): ").strip()
        if port_input.isdigit() and 1 <= int(port_input) <= 65535:
            port = int(port_input)
            break
        else:
            print("Ошибка: введите корректный номер порта (число от 1 до 65535).")

    # Создаём сокет
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        try:
            # Привязка сокета к хосту и порту
            sock.bind((host, port))
            # Прослушивание порта
            sock.listen(1)
            print(f"Сервер запущен на порту {port}.")
            print(f"Прослушивания порта {port}...")

            # Принимаем подключение клиента
            conn, addr = sock.accept()
            print(f"Клиент {addr} подключился к серверу.")

            # Цикл для принятия сообщений
            while True:
                # Принимаем сообщение от клиента порционно
                data = conn.recv(1024)
                if not data:
                    break

                # Проверяем, пришла ли команда "exit"
                if data.decode().strip().lower() == "exit":
                    print(f"Клиент {addr} отправил команду выхода. Отключение клиента...")
                    break

                # Служебное сообщение IV
                print(f"Сервер получил данные от клиента: {data.decode()}")

                # Немного видоизменим возвращаемые данные
                changed_data = f"{data.decode().replace(' ', '...')}..."
                conn.send(changed_data.encode())
                print("Полученные данные были видоизменены и отправлены обратно клиенту.")

            # Закрываем соединение
            print(f"Отключение клиента от сервера...")
            conn.close()
            print(f"Клиент {addr} отключён.")

        # Прерывание программы
        except KeyboardInterrupt:
            print("ВНИМАНИЕ! Принято KeyboardInterrupt.")
            if conn:
                conn.send("ОШИБКА! Сервер был преждевременно остановлен.".encode())

    print("Остановка сервера...")
    print("Сервер остановлен.")

if __name__ == "__main__":
    my_server()
