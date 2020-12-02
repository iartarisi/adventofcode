def fuel(m):
    return int(m) // 3 - 2

def add_fuel(f, m):
    req = fuel(m)
    if req <= 0:
        return f
    else:
        return req + add_fuel(f, req)



with open('1.input') as f:
    answer = sum(add_fuel(0, m) for m in f)

answer
