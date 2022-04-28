#!/usr/bin/python3
"""
This script takes multiple lines of arguments
and does computations for it
"""
import sys

if __name__ == '__main__':

    def stat_compute(status_codes, file_size):
        """ This function reads stdin and computes the metrics """
        print("File size: {:d}".format(file_size))
        for s_code, times in sorted(status_codes.items()):
            if times:
                print("{:s}: {:d}".format(s_code, times))

    status_codes = {"200": 0,
                   "301": 0,
                   "400": 0,
                   "401": 0,
                   "403": 0,
                   "404": 0,
                   "405": 0,
                   "500": 0
                   }
    file_size = 0
    n_lines = 0

    try:
        for line in sys.stdin:
            if n_lines != 0 and n_lines % 10 == 0:
                """ Read 10 lines, and print from the beginning """
                stat_compute(status_codes, file_size)
            n_lines += 1
            data = line.split()
            try:
                s_code = data[-2]
                if s_code in status_codes:
                    status_codes[s_code] += 1
                file_size += int(data[-1])
            except:
                pass
        stat_compute(status_codes, file_size)
    except KeyboardInterrupt:
        stat_compute(status_codes, file_size)
        raise
