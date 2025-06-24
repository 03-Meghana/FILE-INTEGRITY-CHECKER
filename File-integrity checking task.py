import hashlib
import os
import json
import shutil
import time
import argparse
from datetime import datetime
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text
from tqdm import tqdm
from colorama import Fore, Style, init as colorama_init

colorama_init(autoreset=True)
console = Console()

HASH_LOG_FILE = 'file_hashes.json'
LOG_FILE = 'integrity_log.txt'
BLOCK_SIZE = 4096
SKIP_EXTENSIONS = ['.tmp', '.log']
SKIP_DIRS = ['__pycache__', '.git']

def log_event(message: str):
    """Log an event with timestamp to a file."""
    with open(LOG_FILE, 'a', encoding='utf-8') as f:
        f.write(f"[{datetime.now()}] {message}\n")

def get_sha256_hash(file_path: str) -> str:
    """Generate the SHA-256 hash of a file."""
    sha256 = hashlib.sha256()
    try:
        with open(file_path, 'rb') as f:
            for block in iter(lambda: f.read(BLOCK_SIZE), b''):
                sha256.update(block)
        return sha256.hexdigest()
    except Exception as e:
        console.print(f"[red][ERROR][/red] {file_path}: {e}")
        return None

def load_previous_hashes():
    if os.path.exists(HASH_LOG_FILE):
        with open(HASH_LOG_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}

def save_current_hashes(hashes):
    if os.path.exists(HASH_LOG_FILE):
        shutil.copy(HASH_LOG_FILE, HASH_LOG_FILE + '.bak')
    with open(HASH_LOG_FILE, 'w', encoding='utf-8') as f:
        json.dump(hashes, f, indent=4)

def tree_print(path):
    """Print a simplified tree structure from a full path."""
    parts = path.strip(os.sep).split(os.sep)
    indent = "  " * (len(parts) - 1)
    return f"{indent}└── {parts[-1]}"

def scan_directory(folder_path):
    start_time = time.time()
    stored_hashes = load_previous_hashes()
    latest_hashes = {}
    new_files = modified_files = deleted_files = 0
    total_files = 0

    console.print(Panel(f"Scanning [bold]{folder_path}[/bold]...", title="🔍 Scan Started", style="blue"))
    log_event(f"Started scan for: {folder_path}")

    file_paths = []
    for root, dirs, files in os.walk(folder_path):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        for file in files:
            if any(file.lower().endswith(ext) for ext in SKIP_EXTENSIONS):
                continue
            file_paths.append(os.path.join(root, file))

    for file_path in tqdm(file_paths, desc="Checking files", colour="cyan"):
        file_hash = get_sha256_hash(file_path)
        total_files += 1
        if not file_hash:
            continue
        latest_hashes[file_path] = file_hash

        if file_path not in stored_hashes:
            console.print(f"[green][NEW][/green] {tree_print(file_path)}")
            log_event(f"[NEW FILE] {file_path}")
            new_files += 1
        elif stored_hashes[file_path] != file_hash:
            console.print(f"[yellow][MODIFIED][/yellow] {tree_print(file_path)}")
            log_event(f"[MODIFIED] {file_path}")
            modified_files += 1

    for old_path in stored_hashes:
        if old_path not in latest_hashes:
            console.print(f"[red][DELETED][/red] {tree_print(old_path)}")
            log_event(f"[REMOVED] {old_path}")
            deleted_files += 1

    save_current_hashes(latest_hashes)

    elapsed = round(time.time() - start_time, 2)

    table = Table(title="📊 Summary Report", style="bold")
    table.add_column("Type", style="cyan", justify="right")
    table.add_column("Count", style="bold white", justify="center")
    table.add_row("New Files", str(new_files))
    table.add_row("Modified", str(modified_files))
    table.add_row("Deleted", str(deleted_files))
    table.add_row("Total Scanned", str(total_files))
    table.add_row("Time Taken", f"{elapsed} sec")
    console.print(table)

    if new_files + modified_files + deleted_files == 0:
        console.print(Panel("[green]🎉 No changes detected![/green] Your files are safe and unchanged.",
                            title="Integrity Check Passed", style="green"))

def main():
    parser = argparse.ArgumentParser(description="Smart File Integrity Checker")
    parser.add_argument('-p', '--path', help="Path to folder to scan", required=False)
    args = parser.parse_args()

    folder = args.path or input("📁 Enter the folder path to scan: ").strip()
    if not os.path.isdir(folder):
        console.print("[red][ERROR][/red] That path is not valid.")
        return

    scan_directory(folder)

if __name__ == '__main__':
    main()
