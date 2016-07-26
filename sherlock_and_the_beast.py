def decent(digit):
    if digit < 3:
        return -1
    elif not digit % 3:
        return int(str(5) * digit)
    elif digit == 5:
        return int(str(3) * digit)
    else:
        trigger = False
        for values in range(digit/3, -1, -1):
            if not (digit - (3 * values)) % 5:
                trigger = True
                return int(str(5) * (3 * values) + str(3) * (digit - (3 * values)))
                break
        if not trigger:
            return -1
                
t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())
    print decent(n)
