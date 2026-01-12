# Bruteforce Detector (Python)

## Overview

This tool analyzes authentication logs and detects potential brute-force attacks based on repeated failed login attempts.
If an identifier exceeds a defined failure threshold, it is flagged as suspicious.

## How it works

* Reads a log file line by line
* Identifies failed login events using the string `Login failed`
* Extracts an identifier:

  * Uses `user=` when present and non-empty
  * Falls back to `ip=` if the user is missing
  * Ignores entries without valid identifiers
* Counts failed attempts per identifier
* Flags identifiers whose failures meet or exceed the threshold

## Input format

Each log entry is a single line of text.
Relevant tokens:

* `Login failed`
* `user=<username>`
* `ip=<ip_address>`

Example:

```
2026-01-10 10:15:23 INFO Login failed user=admin ip=10.0.0.5
```

## How to run

1. Place the log file as `sample.log` in this folder.
2. Run:

```
python main.py
```

## Output

Prints a list of identifiers suspected of brute-force activity:

```
Bruteforce suspects (threshold=3):
Identifier: admin Fails: 5
Identifier: 10.0.0.5 Fails: 3
```

If no suspects are detected, a message is displayed.

## Design decisions

* A simple threshold-based approach is used for clarity and reliability.
* `unknown` identifiers are excluded to avoid false positives.
* The tool is designed as a lightweight, internal security utility.

## Next improvements

* Make the threshold configurable via command-line arguments
* Sort suspects by highest number of failures
* Support multiple log formats
* Export results to a file (CSV/JSON)
