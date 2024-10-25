#!/usr/bin/python3
'''

0-stats.py

'''
import sys
import re


if __name__ == "__main__":
    codes = ['200', '301', '400', '401', '403', '404', '405', '500']
    code_stats = {code: 0 for code in codes}
    reg = re.compile(r'''
    ^
    (\d{1,3}\.){3}\d{1,3}
    \s-\s
    \[\d{4}-\d{2}-\d{2}
    \s\d{2}:\d{2}:\d{2}\.\d+\]
    \s"GET\s\/projects\/260\s
    HTTP\/1\.1"\s
    (200|301|400|401|403|404|405|500)
    \s\d+$
    ''', re.VERBOSE)
    line_count = 0
    file_size = 0

    def print_stats() -> None:
        '''prints current stats'''
        print('File size: {:d}'.format(file_size))
        for code, calls in sorted(code_stats.items()):
            if calls:
                print('{}: {}'.format(code, calls))

    try:
        for line in sys.stdin:
            if reg.match(line):
                line_count += 1
                data = line.split()
                status_code = data[-2]
                code_stats[status_code] += 1
                file_size += int(data[-1])
            if line_count % 10 == 0:
                print_stats()
        print_stats()
    except KeyboardInterrupt:
        print_stats()
        raise
