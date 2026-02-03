import time
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# ✅ Replace this with your actual project path
PROJECT_PATH = r"C:\Users\Hp\PycharmProjects\Mursalin_Python"

class GitAutoUploader(FileSystemEventHandler):
    def on_modified(self, event):
        if event.is_directory:
            return
        print(f"Detected change in: {event.src_path}")
        try:
            os.system(f'cd "{PROJECT_PATH}" && git add . && git commit -m "Auto update" && git push origin main')
            print("✅ Auto-pushed changes to GitHub.")
        except Exception as e:
            print("❌ Error pushing:", e)

if __name__ == "__main__":
    print(f"👀 Watching: {PROJECT_PATH}")
    event_handler = GitAutoUploader()
    observer = Observer()
    observer.schedule(event_handler, path=PROJECT_PATH, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(5)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

