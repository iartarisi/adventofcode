import re

inputfile = """
1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc
"""

def silver():
    corrects = 0
    with open('2.input') as f:
        for l in f:
            if l:
                minimum, maximum, char, password = re.match("(\d+)-(\d+) ([a-z]): (\w+)", l).groups()
                minimum = int(minimum)
                maximum = int(maximum)
                occurences = 0
                for c in password:
                    if c == char:
                        occurences += 1
                        if occurences > maximum:
                            break
                else:
                    if occurences >= minimum:
                        print(l)
                        corrects += 1

def gold():
    corrects = 0
    with open('2.input') as f:
        for l in f:
            first, second, char, password = re.match("(\d+)-(\d+) ([a-z]): (\w+)", l).groups()
            first = int(first)
            second = int(second)

            if (password[first-1] == char) ^ (password[second-1] == char):
                corrects += 1

    return corrects

gold()
