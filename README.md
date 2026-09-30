# Python Security Automation

A collection of small Python scripts for security automation: log analysis and file integrity checking. Each project lives in its own folder; folders 01–03 include their own README with more detail.

## Projects

- **01_failed_login_counter** — Reads an authentication log file and counts failed login attempts per identifier (user/IP).
- **02_bruteforce_detector** — Analyzes authentication logs and flags identifiers with repeated failed logins ("Login failed" events on `user=`/`ip=` identifiers) at or above a threshold of 3 as possible brute-force attacks.
- **03_ip_blacklist_checker** — Compares observed IP addresses against a blacklist and writes a structured report of which IPs matched.
- **04_file_integrity_checker** — Snapshots the `watched` directory (SHA-256 hash, size, and mtime per file) into `baseline.json` with `init()`, and later compares a fresh snapshot against that baseline to detect new, deleted, modified, or unreadable files with `check()`.

## Run

Each project is standalone — `cd` into its folder first.

- **01_failed_login_counter** and **02_bruteforce_detector**: place your log file in the folder as `sample.log`, then run:

  ```
  python main.py
  ```

- **03_ip_blacklist_checker**: place `blacklist.txt` (the blacklist) and `sample_ips.txt` (the IPs to check) in the folder, then run the script with Python 3.
- **04_file_integrity_checker**: with Python 3, call `init()` to record a baseline of the `watched` directory, then call `check()` later to compare the current state against that baseline.
