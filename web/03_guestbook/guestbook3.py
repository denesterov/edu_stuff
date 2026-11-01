from http.server import HTTPServer, BaseHTTPRequestHandler
import urllib.parse
import sqlite3


db_conn = None

def init_db():
    global db_conn
    db_conn = sqlite3.connect('guestbook.db')
    db_conn.cursor().execute('''
CREATE TABLE IF NOT EXISTS messages (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    text TEXT,
    time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
''')


def format_page():
    global db_conn

    items = ''

    cursor = db_conn.cursor()
    cursor.execute("SELECT id, text, datetime(time, 'localtime') FROM messages")
    rows = cursor.fetchall()
    for id, text, when in rows:
        items += f'<li>{id}. Аноним в {when} написал:<br>{text}</li>'


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
    if text.strip() == '':
        return
    cursor = db_conn.cursor()
    cursor.execute('INSERT INTO messages (text) VALUES (?)', (text,))
    db_conn.commit()


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
    init_db()
    httpd.serve_forever()
except KeyboardInterrupt:
    print('\nСервер остановлен.')
    httpd.server_close()
    db_conn.close()
