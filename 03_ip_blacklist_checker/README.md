# 03_ip_blacklist_checker

## Description

This tool checks a list of IP addresses against a blacklist and generates a structured report indicating which IPs are blacklisted and which are not.

It is designed as a small, practical automation commonly used in Blue Team / SOC workflows, where analysts need to quickly validate indicators against known malicious sources.

The script reads input files, performs set-based lookups for efficiency, and writes a clean, human-readable report to a text file.

## What the script does

* Loads a blacklist of IP addresses from `blacklist.txt`
* Loads a list of observed IPs from `sample_ips.txt`
* Compares each IP against the blacklist
* Separates IPs into:

  * Blacklisted
  * Not blacklisted
* Generates a report file (`results.txt`) with:

  * Clear sections
  * One IP per line
  * Explicit handling of empty results (`NONE`)
  * Total counts per section

## Input files

* `blacklist.txt`
  One IP address per line. Empty lines are ignored.

* `sample_ips.txt`
  One IP address per line representing observed traffic or events.

## Output file

* `results.txt`

Example output:

```
BLACKLISTED:
192.168.1.10
10.0.0.5
Total blacklisted: 2

NOT BLACKLISTED:
8.8.8.8
1.1.1.1
Total not blacklisted: 2
```

If a section has no entries, it is explicitly reported as:

```
NONE
Total blacklisted: 0
```

## Concepts practiced

* File reading and writing
* Defensive string handling (`strip`)
* Difference between `list` and `set`
* Efficient membership testing
* Separation of logic and output
* Deterministic, readable reporting
* Handling edge cases (empty inputs)

## How to run

1. Place `blacklist.txt` and `sample_ips.txt` in the same directory as the script
2. Run the script with Python 3
3. Review the generated `results.txt`

## Why this tool matters

This script reflects a real-world task often performed in security operations: validating indicators of compromise against known threat intelligence lists.

It prioritizes clarity, correctness, and maintainability over abstraction.
