from copy import deepcopy
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

def validate_hgt(hgt):
    try:
        number, scale = re.fullmatch('(\d+)(cm|in)$', hgt).groups()
    except AttributeError:
        return False

    if scale == 'cm':
        return 150 <= int(number) <= 193
    else:
        return 59 <= int(number) <= 76

validators = {
    'byr': lambda x: 1920 <= int(x) <= 2002,
    'iyr': lambda x: 2010 <= int(x) <= 2020,
    'eyr': lambda x: 2020 <= int(x) <= 2030,
    'hgt': validate_hgt,
    'hcl': lambda x: re.fullmatch('#[0-9a-f]{6}', x),
    'ecl': lambda x: x in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'],
    'pid': lambda x: re.fullmatch('[0-9]{9}', x),
}

def split_passports(input):
    return input.split('\n\n')

def count_valid(input):
    count = 0
    for passport in split_passports(input):
        valids = deepcopy(validators)
        fields = re.findall("(\w+):(\S+)", passport)
        # print('passport: ', passport, '\n')
        for key, value in fields:
            if key == 'cid':
                continue
            try:
                validator = valids.pop(key)
            except KeyError:
                break

            if not validator(value):
                # print('invalid ', key, value)
                break
        else:
            if not valids:
                print('passport: ', passport)
                count += 1
    return count


invalid_example = """
eyr:1972 cid:100
hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926

iyr:2019
hcl:#602927 eyr:1967 hgt:170cm
ecl:grn pid:012533040 byr:1946

hcl:dab227 iyr:2012
ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

hgt:59cm ecl:zzz
eyr:2038 hcl:74454a iyr:2023
pid:3556412378 byr:2007

eyr:2029 ecl:blu cid:129 byr:1989
iyr:2014 pid:896056539 hcl:#a97842
"""

valid_example = """
pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
hcl:#623a2f

eyr:2029 ecl:blu cid:129 byr:1989
iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

hcl:#888785
hgt:164cm byr:2001 iyr:2015 cid:88
pid:545766238 ecl:hzl
eyr:2022

iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719
"""

assert count_valid(invalid_example) == 0
assert count_valid(valid_example) == 4

with open('4.input') as f:
    batchfile = f.read()
    print(count_valid(batchfile))
