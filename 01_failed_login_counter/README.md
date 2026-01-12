Title: Failed Login Counter (Python)

What it does
Reads a log file and counts failed login attempts per identifier. If a valid user= value is present, it counts by user; otherwise it falls back to ip=. If neither is present, it uses unknown.

Input format
Each log entry is a line of text. Failed attempts are identified by the substring Login failed. Example tokens: user=<name> and ip=<address>.

How to run

Place the log file as sample.log in this folder.

Run: python main.py

Output
Prints a summary: identifier -> number of failed attempts.

Next improvements (v1.1)

Sort results by highest failures first

Print total failed attempts

Accept log filename via command line argument
