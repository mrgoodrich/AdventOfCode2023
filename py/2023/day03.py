#       --------Part 1--------   --------Part 2--------
# Day       Time   Rank  Score       Time   Rank  Score
#   3   01:08:02   7718      0   01:33:49   7069      0
#   2   00:25:44   5912      0   00:31:01   5415      0
#   1   09:17:53  73604      0   09:46:40  48789      0

import re
from collections import defaultdict

def p1(f):
    ans = 0

    matched = []

    lines = f.read().splitlines()

    spots = {}

    for row, line in enumerate(lines):
        for col, c in enumerate(line):
            if not c.isdigit() and c != ".":
                spots.update({str(row) + ',' + str(col): 1})

    # print(spots)

    for row, line in enumerate(lines):
        start = -1
        end = 0
        cur = ""
        for col, c in enumerate(line):
            if c.isdigit():
                if start == -1:
                    start = col
                cur += c
            else:
                if cur != "":
                    end = col - 1

                    # print(cur)
                    # print(start)
                    # print(end)

                    match = False
                    for a in range(start - 1, end + 2):
                        for r in range(row - 1, row + 2):
                            if a >= 0 and a < len(line) and r >= 0 and r < len(lines):
                                # print('checking ' + str(r) + ',' + str(a))
                                if str(r) + ',' + str(a) in spots:
                                    match = True
                                    # print('match ' + str(r) + ', ' + str(a))

                    if match:
                        # print('adding ' + cur)
                        matched.append(cur)
                        ans += int(cur)
                    # else:
                        # print('not adding ' + cur)

                    cur = ""
                    start = -1
        if cur != "":
            end = len(line) - 1
            # print(cur)
            # print(start)
            # print(end)

            match = False
            for a in range(start - 1, end + 2):
                for r in range(row - 1, row + 2):
                    if a >= 0 and a < len(line) and r >= 0 and r < len(lines):
                        # print('checking ' + str(r) + ',' + str(a))
                        if str(r) + ',' + str(a) in spots:
                            match = True
                            # print('match ' + str(r) + ', ' + str(a))
            if match:
                # print('adding ' + cur)
                matched.append(cur)
                ans += int(cur)

        # nums = re.findall(r"\d+", line)
        # print(nums)

    # print(matched)

    return ans



gears = defaultdict(list)

def registerGear(row, col, number):
    gears[row + ',' + col].append(number)

def p2(f):
    ans = 0

    matched = []

    lines = f.read().splitlines()

    spots = {}

    for row, line in enumerate(lines):
        for col, c in enumerate(line):
            if not c.isdigit() and c != ".":
                spots.update({str(row) + ',' + str(col): c})

    # print(spots)

    for row, line in enumerate(lines):
        start = -1
        end = 0
        cur = ""
        for col, c in enumerate(line):
            if c.isdigit():
                if start == -1:
                    start = col
                cur += c
            else:
                if cur != "":
                    end = col - 1
                    #
                    # print(cur)
                    # print(start)
                    # print(end)

                    match = False
                    for a in range(start - 1, end + 2):
                        for r in range(row - 1, row + 2):
                            if a >= 0 and a < len(line) and r >= 0 and r < len(lines):
                                # print('checking ' + str(r) + ',' + str(a))
                                if str(r) + ',' + str(a) in spots and spots[str(r) + ',' + str(a)] == '*':
                                    registerGear(str(r), str(a), cur)

                    cur = ""
                    start = -1
        if cur != "":
            end = len(line) - 1
            # print(cur)
            # print(start)
            # print(end)

            match = False
            for a in range(start - 1, end + 2):
                for r in range(row - 1, row + 2):
                    if a >= 0 and a < len(line) and r >= 0 and r < len(lines):
                        # print('checking ' + str(r) + ',' + str(a))
                        if str(r) + ',' + str(a) in spots and spots[str(r) + ',' + str(a)] == '*':
                            registerGear(str(r), str(a), cur)

        # nums = re.findall(r"\d+", line)
        # print(nums)

    # print(matched)

    # print(gears)
    for gear, nums in gears.items():
        if (len(nums) == 2):
            ans += int(nums[0]) * int(nums[1])

    return ans
