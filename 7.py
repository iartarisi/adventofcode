from copy import deepcopy
from collections import defaultdict
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

def load_rules(rules):
    rs = defaultdict(list)
    for rule in rules:
        if not rule or rule =='\n':
            continue

        groups = re.match("(\w+ \w+) bags contain (?:\d (\w+ \w+) bag[s]*(?:, \d (\w+ \w+) bag[s]*)?|no other bags).", rule).groups()

        rs[groups[0]] = groups[1:]

    return rs


def has_shiny_gold(rules, bag):
    if bag == 'shiny gold':
        return True

    return any(has_shiny_gold(rules, b) for b in rules[bag])

rules = load_rules(rules_file.splitlines())
sum(has_shiny_gold(deepcopy(rules), b) for b in rules) - 1
with open('7.input') as f:
    rules = load_rules(f.readlines())
    print(sum(has_shiny_gold(deepcopy(rules), b) for b in rules) - 1)

