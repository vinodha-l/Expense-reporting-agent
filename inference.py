import http.server, socketserver, json
class SimpleHTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Running")
    def do_POST(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps({"status": "success"}).encode())
if __name__ == "__main__":
    socketserver.TCPServer(("", 7860), SimpleHTTPRequestHandler).serve_forever()
