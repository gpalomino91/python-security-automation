import os
import hashlib
import json

def init():
    base_dir = "watched"

    if not os.path.isdir(base_dir):
        print("Directory not found")
        return

    baseline_data = {}

    for current_dir, subdirs, files in os.walk(base_dir):

        for file in files:
            full_path = os.path.join(current_dir, file)
            rel_path = os.path.relpath(full_path, base_dir)

            size = os.path.getsize(full_path)
            mtime = os.path.getmtime(full_path)
            sha256 = sha256_file(full_path)

            baseline_data[rel_path] = {
                "size": size,
                "mtime": mtime,
                "sha256": sha256
            }
    with open("baseline.json", "w", encoding="utf-8") as f:
        json.dump(baseline_data, f, indent=2, sort_keys=True)

def sha256_file(full_path, chunk_size=8192):
    h = hashlib.sha256()
    try:
        with open(full_path, "rb") as f:
            while True:
                chunk = f.read(chunk_size)
                if not chunk:
                    break
                h.update(chunk)
            return h.hexdigest()
    except (OSError, PermissionError):
        return None

