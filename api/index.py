import subprocess
import http.server
import socketserver

class TranslatorHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            # Run the Streamlit app as a subprocess
            subprocess.Popen(['streamlit', 'run', 'app.py'])
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b'Streamlit app is running...')
        else:
            # Serve other files as usual
            super().do_GET()

# Define the server address and port
host = "http://127.0.0.1"
port = 8501

# Create and start the HTTP server
with socketserver.TCPServer((host, port), TranslatorHandler) as httpd:
    print(f'Serving on {host}:{port}')
    httpd.serve_forever()
