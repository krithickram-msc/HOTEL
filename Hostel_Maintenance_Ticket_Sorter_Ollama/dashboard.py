from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import csv, json, webbrowser, threading

ROOT = Path(__file__).resolve().parent
HOST, PORT = "127.0.0.1", 8765

def read_rows(name):
    path = ROOT / name
    if not path.exists():
        return []
    try:
        with path.open(newline="", encoding="utf-8-sig") as f:
            return list(csv.DictReader(f))
    except (OSError, csv.Error):
        return []

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/api/data":
            payload = {"work_orders": read_rows("work_orders.csv"),
                       "results": read_rows("results.csv"),
                       "needs_info": read_rows("needs_info.csv")}
            body = json.dumps(payload).encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Cache-Control", "no-store")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
            return
        if self.path in ("/", "/index.html"):
            body = (ROOT / "dashboard.html").read_bytes()
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
            return
        self.send_error(404)
    def log_message(self, *_):
        pass

if __name__ == "__main__":
    url = f"http://{HOST}:{PORT}"
    server = ThreadingHTTPServer((HOST, PORT), Handler)
    print("Hostel Maintenance Dashboard is running.")
    print("Open this address in your browser:", url)
    print("Keep this window open while using the dashboard. Press Ctrl+C to stop.")
    threading.Timer(1.0, lambda: webbrowser.open(url)).start()
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nDashboard stopped.")
        server.server_close()
