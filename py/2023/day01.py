#       --------Part 1--------   --------Part 2--------
# Day       Time   Rank  Score       Time   Rank  Score
#   1   09:17:53  73604      0   09:46:40  48789      0

# Started morning after

def p1(f):
    ans = 0

    for line in f:
        for ndx in range(len(line)):
            char = line[ndx]
            if char.isdigit():
                f = line[ndx]
                break

        for ndx in reversed(range(len(line))):
            char = line[ndx]
            if char.isdigit():
                l = line[ndx]
                break

        c = str(f) + str(l)
        ans += int(c)

    return ans

numbers = [
    'zero',
    'one',
    'two',
    'three',
    'four',
    'five',
    'six',
    'seven',
    'eight',
    'nine'
]

def p2(f):
    ans = 0

    for line in f:
        for ndx in range(len(line)):
            char = line[ndx]
            if char.isdigit():
                f = line[ndx]
                break
            else:
                lineWordNum = getLineWordNum(line, ndx)
                if lineWordNum != -1:
                    f = lineWordNum
                    break

        for ndx in reversed(range(len(line))):
            char = line[ndx]
            if char.isdigit():
                l = line[ndx]
                break
            else:
                lineWordNum = getLineWordNum(line, ndx)
                if lineWordNum != -1:
                    l = lineWordNum
                    break

        c = str(f) + str(l)
        ans += int(c)
    return ans

def getLineWordNum(line, ndx):
    for numNdx, num in enumerate(numbers):
        if line[ndx:(ndx+len(num))] == num:
            return numNdx
    return -1
