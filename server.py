"""学习手记 - 本地服务器
运行后在同WiFi下用手机浏览器访问即可添加到主屏幕。
"""
import http.server
import socketserver
import socket
import os

PORT = 8080
DIR = os.path.dirname(os.path.abspath(__file__))
os.chdir(DIR)

class Handler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-cache')
        super().end_headers()

print(f'学习手记 PWA 服务器启动...')
print(f'本机访问: http://localhost:{PORT}/study-planner.html')
print(f'手机访问: http://{socket.gethostbyname(socket.gethostname())}:{PORT}/study-planner.html')
print(f'按 Ctrl+C 停止')

with socketserver.TCPServer(("0.0.0.0", PORT), Handler) as httpd:
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print('\n服务器已停止')
