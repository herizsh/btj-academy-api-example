from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def _set_headers(self, status_code=200):
        self.send_response(status_code)
        self.send_header("Content-type", "application/json")
        self.end_headers()

    def do_GET(self):
        if self.path == "/":
            self._set_headers()
            response = {"message": "This is the root path. Hello!"}
        elif self.path == "/hello":
            self._set_headers()
            response = {"message": "Hello from the /hello path!"}
        else:
            self._set_headers(404)
            response = {"error": "Path not found"}

        self.wfile.write(json.dumps(response).encode("utf-8"))

    def do_POST(self):
        if self.path == "/echo":
            content_length = int(self.headers["Content-Length"])
            post_data = self.rfile.read(content_length)
            data = json.loads(post_data)

            self._set_headers()
            response = {"message": "POST request received on /echo", "data": data}
        else:
            self._set_headers(404)
            response = {"error": "Path not found"}

        self.wfile.write(json.dumps(response).encode("utf-8"))


def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler, port=8000):
    server_address = ("", port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting httpd server on port {port}")
    httpd.serve_forever()


if __name__ == "__main__":
    run()
