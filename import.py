import http.server
import socketserver

PORT = 6468

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving at http://localhost:{PORT}")
    httpd.serve_forever()

# to run type 'python import.py' in VS code terminal