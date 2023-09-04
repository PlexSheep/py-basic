import http.server
import io
class MyHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_head()
    def send_head(self):
        body = "hello world"
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        return io.StringIO(body)
addtrss = ("127.0.0.1", 8080)
srv = http.server.HTTPServer(addtrss, MyHandler)
srv.serve_forever()

