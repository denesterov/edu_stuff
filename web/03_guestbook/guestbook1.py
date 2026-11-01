from http.server import HTTPServer, BaseHTTPRequestHandler


html_page = f"""<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>Гестбук</title>
</head>
<body>
    <h2>Гестбук</h2>
    <p>Добро пожаловать! Пишите тут, что думаете...</p>
    <ul class="scroll-list">
        <li>Сообщение 1</li>
        <li>Сообщение 2</li>
        <li>Сообщение 3</li>
    </ul>

    <form action="/">
        <input type="text" placeholder="Введите текст здесь..." /input>
        <button>Отправить</button>
    </form>
</body>
</html>
"""


class MyRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        global session_log

        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        response_text = html_page
        self.wfile.write(response_text.encode("utf-8"))


httpd = HTTPServer(("", 8000), MyRequestHandler)
print("Сервер запущен!")

try:
    httpd.serve_forever()
except KeyboardInterrupt:
    print("\nСервер остановлен.")
    httpd.server_close()
