import re

batchfile = """
ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in
"""

required_fields = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
optional_fields = {'cid'}


def split_passports(input):
    return input.split('\n\n')

def count_valid(input):
    count = 0
    for passport in split_passports(input):
        fields = re.findall("(\w+):\S+", passport)
        count += required_fields.issubset(set(fields))
    return count


with open('4.input') as f:
    batchfile = f.read()
    print(count_valid(batchfile))
