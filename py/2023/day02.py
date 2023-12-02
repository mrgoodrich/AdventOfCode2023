#       --------Part 1--------   --------Part 2--------
# Day       Time   Rank  Score       Time   Rank  Score
#   2   00:25:44   5912      0   00:31:01   5415      0
#   1   09:17:53  73604      0   09:46:40  48789      0

def p1(f):
    ans = 0

    lines = f.read().splitlines()

    for ndx, line in enumerate(lines):
        good = True

        rest = line.split(": ",1)[1]
        each = rest.split(";")

        for one in each:
            red = 12
            green = 13
            blue = 14

            trim = one.strip()
            colors = trim.split(",")
            for pair in colors:
                trim2spl = pair.strip().split(" ")
                qty = int(trim2spl[0])
                color = trim2spl[1]

                if color == 'red' and qty > 12:
                    good = False
                elif color == 'green' and qty > 13:
                    good = False
                elif color == 'blue' and qty > 14:
                    good = False

        if good:
            ans += ndx + 1

    return ans


def p2(f):
    ans = 0

    lines = f.read().splitlines()

    for ndx, line in enumerate(lines):
        red = 0
        green = 0
        blue = 0

        rest = line.split(": ",1)[1]
        each = rest.split(";")

        for one in each:
            trim = one.strip()
            colors = trim.split(",")
            for pair in colors:
                trim2spl = pair.strip().split(" ")
                qty = int(trim2spl[0])
                color = trim2spl[1]

                if color == 'red' and qty > red:
                    red = qty
                elif color == 'green' and qty > green:
                    green = qty
                elif color == 'blue' and qty > blue:
                    blue = qty

        power = red * green * blue
        ans += power

    return ans
