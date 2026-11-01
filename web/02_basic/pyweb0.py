import http.server


class MyRequestHandler(http.server.BaseHTTPRequestHandler):
    # Обработка входящих GET-запросов
    def do_GET(self):
        global COUNTER

        self.send_response(200)
        self.send_header("Content-type", "text/plain; charset=ascii")
        self.end_headers()

        response_text = f"Hello from dummy web server!"
        self.wfile.write(response_text.encode("utf-8"))


httpd = http.server.HTTPServer(("", 8000), MyRequestHandler)
print("Сервер запущен!")

try:
    httpd.serve_forever()
except KeyboardInterrupt:
    print("\nСервер остановлен.")
    httpd.server_close()
