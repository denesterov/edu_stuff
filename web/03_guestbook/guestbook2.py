from http.server import HTTPServer, BaseHTTPRequestHandler
import urllib.parse
import datetime


Messages = []


def format_page():
    items = ''
    for when, text in Messages:
        items += f'<li>Аноним в {when} написал:<br>{text}</li>'

    text = f"""<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>Гестбук</title>
</head>
<body>
    <h2>Гестбук</h2>
    <p>Добро пожаловать! Пишите тут, что думаете...</p>
    <ul class="scroll-list">
        {items}
    </ul>

    <form action="/" method="POST">
        <input type="text" name="user_text" placeholder="Введите текст здесь..." /input>
        <button type="submit">Отправить</button>
    </form>
</body>
</html>
"""
    return text


def store_message(text: str):
    global Messages

    if text.strip() == '':
        return
    when = datetime.datetime.now()
    when_str = when.strftime("%Y-%m-%d %H:%M:%S")

    Messages.append((when_str, text))


class MyRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-Type', 'text/html; charset=utf-8')
        self.end_headers()
        response_text = format_page()
        self.wfile.write(response_text.encode("utf-8"))


    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        post_data_str = post_data.decode('utf-8')

        parsed_data = urllib.parse.parse_qs(post_data_str)
        
        # Достаем текст из поля по его имени 'user_text'. возвращает список, поэтому берем первый элемент [0]
        user_text = parsed_data.get('user_text', [''])[0]

        print(f'\n[ПОЛУЧЕН POST-ЗАПРОС] Текст от пользователя: {user_text}\n')
        store_message(user_text)
        
        # Отправляем ответ
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        response_text = f"<p>Сообщение отправлено! <a href='/'>Назад</a>"
        self.wfile.write(response_text.encode('utf-8'))


httpd = HTTPServer(('', 8000), MyRequestHandler)
print('Сервер запущен!')

try:
    httpd.serve_forever()
except KeyboardInterrupt:
    print('\nСервер остановлен.')
    httpd.server_close()
