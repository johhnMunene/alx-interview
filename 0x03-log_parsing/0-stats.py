#!/usr/bin/python3
"""Python script that reads stdin line by line and computes metrics"""

import sys


def print_metrics(total_file_size, status):
    """Prints total file size and status list"""
    print("File size: {:d}".format(total_file_size))
    for key, value in sorted(status.items()):
        if value != 0:
            print("{}: {}".format(key, value))


status = {'200': 0, '301': 0, '400': 0, '401': 0,
          '403': 0, '404': 0, '405': 0, '500': 0}

total_file_size = 0
line_count = 0
try:
    for line in sys.stdin:
        line = line.strip()  # Remove leading/trailing whitespaces

        # Split line into components
        parts = line.split()
        
        # Ensure the line has the expected format
        if len(parts) >= 7 and parts[-3].isdigit() and parts[-2] in status:
            status_code = parts[-2]
            file_size = int(parts[-1])

            status[status_code] += 1
            total_file_size += file_size
            line_count += 1

            # Print metrics after every 10 lines
            if line_count % 10 == 0:
                print_metrics(total_file_size, status)

except KeyboardInterrupt:
    pass

finally:
    print_metrics(total_file_size, status)
