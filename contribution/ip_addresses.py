# Count the maximal number of IP addresses possible to compose with given mask

s = "1234.1001.1001.0000"  # "1234.0000.0000.0000"

n = 0
for idx, x in enumerate(s[::-1]):
    if idx % 5 != 4:
        if x == '0':
            n += 1
        else:
            break

print(int('1' + n*'0'))
