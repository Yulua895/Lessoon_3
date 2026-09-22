import socket



ip = '127.0.0.1'
port = 9001
endpoint = (ip, port)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    client.connect(endpoint)  # подключение к серверу
    while True:
        client_message = input('Сообщение серверу: ')
        client.send(client_message.encode(encoding='utf-8'))
        if client_message == 'stop_server':
            break
        # прием сообщения
        server_message = client.recv(1024).decode(encoding='utf-8')
        print(f'Ответ сервера: {server_message}')

        _continue = input('Продолжать обмен (n/y)?: ')
        if _continue == 'n':
            break
except BaseException as err:
    print(err)
finally:
    client.close()
