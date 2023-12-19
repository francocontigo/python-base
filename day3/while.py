n = 0
while n < 101:
    if n >= 40 and n <= 60:
        n += 1
        continue
    if n == 80:
        break
    print(n)
    n += 1

