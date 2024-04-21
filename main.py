import requests
import threading
import http.server
import socketserver

def run_serv():

    PORT = 8000

    Handler = http.server.SimpleHTTPRequestHandler

    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print("Сервер запущен на порту", PORT)
        httpd.serve_forever()


    # Запуск локального сервера в отдельном потоке
server_thread = threading.Thread(target=run_serv)
server_thread.start()

    




