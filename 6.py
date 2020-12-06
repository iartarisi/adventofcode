from io import StringIO

test = StringIO("""
abc

a
b
c

ab
ac

a
a
a
a

b""")

def count_group_answers(lines):
    score = 0
    group_answers = []
    for line in lines:
        if line == '\n' and group_answers:
            score += len(set.intersection(*group_answers))
            group_answers = []

        if line.strip():
           group_answers.append(set(line.strip()))
        
    # there's no newline after the last group
    score += len(set.intersection(*group_answers))
    return score


print(count_group_answers(test))
with open('6.input') as f:
    score = count_group_answers(f)
    print(score)
