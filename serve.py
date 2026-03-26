#!/usr/bin/env python3
"""Simple local server for the resume renderer.

Usage:
    python3 serve.py [port]

Serves resume-renderer.html at http://localhost:<port>/
Default port is 8000.
"""

import http.server
import os
import sys

PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8000
DIRECTORY = os.path.dirname(os.path.abspath(__file__))
RESUME_FILE = "resume-renderer.html"


class ResumeHandler(http.server.SimpleHTTPRequestHandler):
    """Routes / to resume-renderer.html; serves other files normally."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def do_GET(self):
        if self.path == "/":
            self.path = f"/{RESUME_FILE}"
        return super().do_GET()


def main():
    with http.server.HTTPServer(("", PORT), ResumeHandler) as server:
        url = f"http://localhost:{PORT}/"
        print(f"Serving resume at {url}")
        print("Press Ctrl+C to stop.")
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            print("\nServer stopped.")


if __name__ == "__main__":
    main()
