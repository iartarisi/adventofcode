from copy import deepcopy
from pprint import pprint
import re

rules_file = """
light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags."""

example2 = """
shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags.
"""

def load_rules(rules):
    rs = {}
    for rule in rules:
        if not rule or rule =='\n':
            continue

        groups = re.match("(\w+ \w+) bags contain (\d .*|no other bags).", rule).groups()
        contents = re.findall("(\d) (\w+ \w+) bag[s]?,?", groups[1])

        rs[groups[0]] = contents

    return rs


def has_shiny_gold(rules, bag, depth=0):
    if bag == 'shiny gold':
        return True

    return any(has_shiny_gold(rules, b, depth+1) for _, b in rules[bag])

def dig_in(rules, color):
    return 1 + sum(int(num) * dig_in(rules, col) for num, col in rules[color])



with open('7.input') as f:
    rules = load_rules(f.readlines())
    print("silver: ", sum(has_shiny_gold(deepcopy(rules), b) for b in rules) - 1)
    print("gold: ", dig_in(rules, 'shiny gold') -1)
