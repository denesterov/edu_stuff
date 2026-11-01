import http.server


COUNTER = 0

class MyRequestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        global COUNTER

        self.send_response(200)
        self.send_header("Content-type", "text/plain; charset=ascii")
        self.end_headers()
        response_text = f"Hello from web server! Counter = {COUNTER}"

        self.wfile.write(response_text.encode("utf-8"))

        COUNTER += 1


httpd = http.server.HTTPServer(("", 8000), MyRequestHandler)
print("Сервер запущен!")

try:
    httpd.serve_forever()
except KeyboardInterrupt:
    print("\nСервер остановлен.")
    httpd.server_close()
