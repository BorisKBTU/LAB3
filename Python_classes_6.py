def find_multipliers(a):
    mult = []
    for i in range(1, a + 1):
        if a % i == 0:
            mult.append(i)
    if len(mult) > 2:
        return False
    return True


a = [i for i in range(1, 100)]
print(a)
print(f'Compound numbers: {list(filter(lambda x: not find_multipliers(x), a))}')
print(f'Prime numbers: {list(filter(lambda x: find_multipliers(x), a))}')
