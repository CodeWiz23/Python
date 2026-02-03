import time
import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

PROJECT_PATH = r"C:\Users\mursa\PycharmProjects\ai_job"
GIT_PATH = r"C:\Program Files\Git\cmd\git.exe"

class GitAutoUploader(FileSystemEventHandler):
    def on_modified(self, event):
        if event.is_directory or ".git" in event.src_path:
            return
        print(f"Detected change in: {event.src_path}")
        # Stage files
        run_git("add", ".")
        # Commit changes (ignore if nothing to commit)
        run_git("commit", "-m", "Auto update")
        # Push to GitHub
        run_git("push", "origin", "main")

def run_git(*args):
    result = subprocess.run([GIT_PATH, "-C", PROJECT_PATH] + list(args), capture_output=True, text=True)
    if result.returncode != 0:
        if "nothing to commit" in result.stderr.lower():
            print("Nothing to commit.")
        else:
            print("❌ Git error:", result.stderr)
    else:
        print(result.stdout)

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
