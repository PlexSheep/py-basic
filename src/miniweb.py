#!/usr/bin/env python3
import http.server
import io

TEXT = """Hello world!

If you're reading this, this web server is working!
"""

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def send_head(self) -> io.BytesIO:
        body = TEXT.encode()
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()

        return io.BytesIO(body)

addtrss = ("127.0.0.1", 8080)
srv = http.server.HTTPServer(addtrss, MyHandler)
srv.serve_forever()

