import sys
import time
import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

WATCH_EXT = (".py", ".kv")


class ReloadHandler(FileSystemEventHandler):
    def __init__(self):
        self.process = subprocess.Popen([sys.executable, "app.py"])

    def on_modified(self, event):
        if event.src_path.endswith(WATCH_EXT):
            print("🔁 Reload:", event.src_path)
            self.restart()

    def restart(self):
        self.process.kill()
        time.sleep(0.5)
        self.process = subprocess.Popen([sys.executable, "app.py"])


if __name__ == "__main__":
    observer = Observer()
    handler = ReloadHandler()

    observer.schedule(handler, ".", recursive=True)
    observer.start()

    print("👀 Dev watcher running (Ctrl+C to stop)")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        handler.process.kill()

    observer.join()
