 #!/usr/bin/python3
import sys
import signal
""" 
Initialize variables to store metrics
"""
total_file_size = 0
status_code_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

def print_statistics():
    global total_file_size
    global status_code_counts
    global line_count

    print("File size:", total_file_size)
    for status_code in sorted(status_code_counts.keys()):
        if status_code_counts[status_code] > 0:
            print("{}: {}".format(status_code, status_code_counts[status_code]))
    print()

def signal_handler(sig, frame):
    print_statistics()
    sys.exit(0)

# Register signal handler for CTRL+C
signal.signal(signal.SIGINT, signal_handler)

for line in sys.stdin:
    line = line.strip()
    parts = line.split()

    if len(parts) != 7:
        continue

    try:
        status_code = int(parts[-2])
        file_size = int(parts[-1])
    except ValueError:
        continue

    # Update metrics
    total_file_size += file_size
    status_code_counts[status_code] += 1
    line_count += 1

    # Print statistics every 10 lines
    if line_count % 10 == 0:
        print_statistics()

