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
vibrant flap bags contain 1 muted yellow bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags."""

def load_rules(rules):
    rs = defaultdict(list)
    for rule in rules:
        if not rule or rule =='\n':
            continue
        try:
            groups = re.match("(\w+ \w+) bags contain (?:\d (\w+ \w+) bag[s]*(?:, \d (\w+ \w+) bag[s]*)?|no other bags).", rule).groups()
        except:
            import pdb;pdb.set_trace()
        for group in groups[1:]:
            if group:
                rs[group].append(groups[0])

    return rs



def find_bags(rules, bag):
    try:
        next_bags = rules[bag]
    except KeyError:
        return []

    ret = set(next_bags + [b for bag in next_bags for b in find_bags(rules, bag)])
    print(bag, ret)
    return ret

rules = load_rules(rules_file.splitlines())
print(find_bags(rules, 'shiny gold'))
len(find_bags(rules, 'shiny gold'))
# with open('7.input') as f:
#     rules = load_rules(f.readlines())
#     print(find_bags(rules, 'shiny gold'))
#     print(len(find_bags(rules, 'shiny gold')))
