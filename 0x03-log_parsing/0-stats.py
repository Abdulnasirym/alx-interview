#!/usr/bin/env python3
"""A python module"""

import sys
import signal
import re


pattern = re.compile(r'^(\d{1,3}\.){3}\d{1,3} - \[.*?\] "GET /projects/260 HTTP/1\.1" (\d{3}) (\d+|-)$')
status_code_counts = {}
valid_status_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
total_file_size = 0
line_count = 0


def print_statistics():
    """Prints accumulated statistics including total file size and counts"""
    global total_file_size, status_code_counts

    print(f"File size: {total_file_size}")
    for code in sorted(status_code_counts):
        if code in valid_status_codes:
            print(f"{code}: {status_code_counts[code]}")


def handler(signal, frame):
    """Handles the keyboard interrupt to print statistics"""
    print_statistics()
    sys.exist(0)


signal.signal(signal.SIGINT, handler)


try:
    for line in sys.stdin:
        match = pattern.match(line.strip())
        if match is None:
            continue
        status_code = match.group(2)
        file_size = match.group(3)
        file_size = int(file_size) if file_size.isdigit() else 0
        total_file_size += file_size

        if status_code in status_code_counts:
            status_code_counts[status_code] += 1
        else:
            status_code_counts[status_code] = 1

        line_count += 1
        if line_count % 10 == 0:
            print_statistics()
except Exception as e:
    print(f"An error occured: {e}")
finally:
    print_statistics()
