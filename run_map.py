#!/usr/bin/env python3
"""
Runs census_map.html in a local web server so the browser can load
all local files (CSS, JS, GeoJSON, CSV, etc.)

Usage:
    python run_html.py
"""

import http.server
import socketserver
import webbrowser
import os

PORT = 8000

# Automatically find your html file
HTML_FILE = "visualization/census_map.html"

if not os.path.exists(HTML_FILE):
    raise FileNotFoundError(f"{HTML_FILE} not found in current directory.")

# Create URL
url = f"http://localhost:{PORT}/{HTML_FILE}"

# Open browser automatically
print(f"Opening {url}")
webbrowser.open(url)

# Start simple HTTP server
handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), handler) as httpd:
    print(f"Serving at http://localhost:{PORT}")
    print("Press CTRL + C to stop the server.")
    httpd.serve_forever()
