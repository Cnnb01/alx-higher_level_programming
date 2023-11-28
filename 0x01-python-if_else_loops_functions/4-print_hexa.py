#!/usr/bin/python3
for i in range(0, 99):
    if i < 10:
        print(f"{i} = 0x{i % 10}")
    elif i == 10:
        print(f"{i} = 0x{chr(97)}")
    elif i == 11:
        print(f"{i} = 0x{chr(98)}")
    elif i == 12:
        print(f"{i} = 0x{chr(99)}")
    elif i == 13:
        print(f"{i} = 0x{chr(100)}")
    elif i == 14:
        print(f"{i} = 0x{chr(101)}")
    elif i == 15:
        print(f"{i} = 0x{chr(102)}")
    else:
        print(f"{i} = {hex(i)}")
