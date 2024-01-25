#!/usr/bin/python3
"""
reads stdin line by line and computes metrics
"""


import sys

status = {'200': 0, '301': 0, '400': 0, '401': 0,
         '403': 0, '404': 0, '405': 0, '500': 0}
total_file_size = 0
counter = 0

try:
    for line in sys.stdin:
        line_list = line.split(" ")
        if len(line_list) > 4:
            num = line_list[-2]
            size = int(line_list[-1])
            if num in status.keys():
                status[num] += 1
            total_file_size += size
            counter += 1

        if counter == 10:
            counter = 0
            print('File size: {}'.format(total_file_size))
            for key, value in sorted(status.items()):
                if value != 0:
                    print('{}: {}'.format(key, value))

except Exception as err:
    pass

finally:
    print('File size: {}'.format(total_file_size))
    for key, value in sorted(status.items()):
        if value != 0:
            print('{}: {}'.format(key, value))
