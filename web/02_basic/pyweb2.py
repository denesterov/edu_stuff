from http.server import HTTPServer, BaseHTTPRequestHandler
import time


session_log = []

class MyRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        global session_log

        when = time.asctime()
        who = self.headers.get('User-Agent', 'Unknown')
        ip = self.client_address
        record = (len(session_log), when, ip, who)

        session_log.append(record)

        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        response_text = f"<h3>Привет от минимального сервера Python!</h3> <p>Всего сессий: {len(session_log)}</p>"

        for rec in session_log:
            response_text += f"<p>{rec}</p>"

        self.wfile.write(response_text.encode("utf-8"))


httpd = HTTPServer(("", 8000), MyRequestHandler)
print("Сервер запущен!")

try:
    httpd.serve_forever()
except KeyboardInterrupt:
    print("\nСервер остановлен.")
    httpd.server_close()
