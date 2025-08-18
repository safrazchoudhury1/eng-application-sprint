import datetime
import pathlib
import random
import threading
import time
import tkinter as tk
from tkinter import filedialog, messagebox

# Log file path relative to this script
LOG_FILE = pathlib.Path(__file__).parent / "upload_log_gui.txt"


def log(msg: str) -> None:
    ts = datetime.datetime.now().isoformat(timespec="seconds")
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"[{ts}] {msg}\n")


def attempt_upload(job_path: str) -> bool:
    """
    Simulate an upload with 50% chance of success.
    In a real application this would perform network I/O.
    """
    return random.random() > 0.5


def upload_with_retries(
    job_path: str, max_retries: int = 5, base_delay: float = 0.5
) -> bool:
    """
    Attempt to upload a job, retrying with exponential backoff if it fails.
    Each attempt is logged. Returns True if upload eventually succeeds.
    """
    delay = base_delay
    for attempt in range(1, max_retries + 1):
        ok = attempt_upload(job_path)
        log(f"{job_path}: attempt {attempt} -> {'OK' if ok else 'FAIL'}")
        if ok:
            return True
        time.sleep(delay)
        delay *= 2
    return False


class UploaderGUI:
    """
    Simple Tkinter GUI for managing and uploading jobs with retries.
    Allows the user to add file paths as jobs and start uploads.
    """

    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("Unstable Internet Uploader")
        self.job_queue = []  # type: list[str]
        self.create_widgets()

    def create_widgets(self) -> None:
        # Listbox to display queued jobs
        frame = tk.Frame(self.root)
        frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        self.listbox = tk.Listbox(frame, width=50)
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = tk.Scrollbar(frame, orient=tk.VERTICAL)
        scrollbar.config(command=self.listbox.yview)
        scrollbar.pack(side=tk.LEFT, fill=tk.Y)
        self.listbox.config(yscrollcommand=scrollbar.set)

        # Buttons
        btn_frame = tk.Frame(self.root)
        btn_frame.pack(pady=5)

        add_btn = tk.Button(btn_frame, text="Add Job", command=self.add_job)
        add_btn.pack(side=tk.LEFT, padx=5)

        start_btn = tk.Button(
            btn_frame, text="Start Uploads", command=self.start_uploads
        )
        start_btn.pack(side=tk.LEFT, padx=5)

        # Output text area to show results
        self.output = tk.Text(self.root, height=10, width=60)
        self.output.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)

    def add_job(self) -> None:
        """Prompt the user to select a file and add it to the job queue."""
        path = filedialog.askopenfilename()
        if path:
            self.job_queue.append(path)
            self.listbox.insert(tk.END, path)

    def start_uploads(self) -> None:
        """Start uploading all queued jobs concurrently."""
        if not self.job_queue:
            messagebox.showinfo("Info", "No jobs to upload.")
            return
        # Launch a thread for each job
        for job in list(self.job_queue):
            t = threading.Thread(target=self.process_job, args=(job,))
            t.daemon = True
            t.start()
        # Clear the queue; threads handle processing
        self.job_queue.clear()

    def process_job(self, job_path: str) -> None:
        """Process a single job and update the output box."""
        success = upload_with_retries(job_path)
        result = "Success" if success else "Failed"
        log(f"{job_path}: {result}")
        self.root.after(0, self._append_result, job_path, result)

    def _append_result(self, job_path: str, result: str) -> None:
        """Append job result to the output widget in the main thread."""
        self.output.insert(tk.END, f"{job_path}: {result}\n")
        self.output.see(tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = UploaderGUI(root)
    root.mainloop()
