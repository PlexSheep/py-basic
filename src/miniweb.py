#!/usr/bin/env python3
import http.server
import io

TEXT = "Python is not so hard"

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def send_head(self) -> io.BytesIO:
        body = TEXT.encode()
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()

        return io.BytesIO(body)

address = ("127.0.0.1", 8080)
srv = http.server.HTTPServer(address, MyHandler)
srv.serve_forever()

# To query your web server go to http://localhost:8080
# OR from CLI and with headers:
# $ curl localhost:8080 -v 
