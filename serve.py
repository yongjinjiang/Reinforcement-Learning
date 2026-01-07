#!/usr/bin/env python3
"""
Simple HTTP server for local development
Usage: python serve.py [port]
Default port: 8000
"""

import http.server
import socketserver
import sys
import webbrowser
import os

# Get port from command line argument or use default
PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8000

# Change to the script's directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Add CORS headers for PyScript
        self.send_header('Cross-Origin-Embedder-Policy', 'require-corp')
        self.send_header('Cross-Origin-Opener-Policy', 'same-origin')
        super().end_headers()

    def log_message(self, format, *args):
        # Custom logging format
        print(f"[{self.log_date_time_string()}] {format % args}")

Handler = MyHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    url = f"http://localhost:{PORT}"
    print("=" * 60)
    print(f"Reinforcement Learning Journey - Dev Server")
    print("=" * 60)
    print(f"Server running at: {url}")
    print(f"Serving directory: {os.getcwd()}")
    print("\nPress Ctrl+C to stop the server\n")
    print("=" * 60)

    # Open browser automatically
    try:
        webbrowser.open(url)
        print(f"Opening {url} in your browser...")
    except:
        print(f"Manually open {url} in your browser")

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n\nServer stopped. Happy learning!")
        sys.exit(0)
