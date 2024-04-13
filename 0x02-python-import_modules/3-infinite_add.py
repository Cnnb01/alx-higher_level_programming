#!/usr/bin/python3
import sys
if __name__ == "__main__":
    count = 0
    if len(sys.argv) < 2:
        print(f"{len(sys.argv) - 1}")
    else:
        for i in range(1, len(sys.argv)):
            count = count + int(sys.argv[i])
        print(count)
