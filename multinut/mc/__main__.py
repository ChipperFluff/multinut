import os
import sys
import time
import signal
import logging
import threading
import tkinter
import argparse

# Suppress Qt platform plugin logs
os.environ["QT_LOGGING_RULES"] = "*.debug=false"
os.environ["QT_QPA_PLATFORM"] = "xcb"  # Fallback if auto fails

import webview as wv
from .web import create_app
from flask import Flask

app: Flask = create_app()

def is_headless() -> bool:
    try:
        tk = tkinter.Tk()
        tk.withdraw()
        tk.update()
        tk.destroy()
        return False
    except:
        return True

def webview_supported() -> bool:
    try:
        import gi
        wv.guilib = 'gtk'
        return True
    except ImportError:
        pass
    try:
        import qtpy
        wv.guilib = 'qt'
        return True
    except ImportError:
        pass
    return False

def run_flask(host, port):
    logging.getLogger('werkzeug').setLevel(logging.ERROR)
    app.run(host=host, port=port)

def run():
    parser = argparse.ArgumentParser()
    parser.add_argument("--port", type=int, default=5000)
    parser.add_argument("--host", type=str, default="127.0.0.1")
    parser.add_argument("--url", type=str)
    parser.add_argument("--no-browser", action="store_true")
    args = parser.parse_args()

    url = args.url or f"http://{args.host}:{args.port}/"

    flask_thread = threading.Thread(target=run_flask, args=(args.host, args.port), daemon=True)
    flask_thread.start()
    time.sleep(1.2)

    if args.no_browser:
        print(f"\n🖥️  GUI disabled. Running at: {url}")
        signal.pause()
        return

    if is_headless():
        print(f"\n🙄 Headless system detected. Open manually: {url}")
        signal.pause()
        return

    if not webview_supported():
        print(f"\n🚫 No GUI backend (GTK/Qt) found. Open manually: {url}")
        signal.pause()
        return

    try:
        wv.create_window("multinut.local 🐿️", url, width=900, height=600, resizable=True)
        wv.start()
    except Exception as e:
        print(f"\n❌ GUI error: {type(e).__name__}: {e}")
        print(f"🌐 Open manually: {url}")
        signal.pause()

if __name__ == "__main__":
    run()
