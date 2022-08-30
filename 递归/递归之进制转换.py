def toStr(n, base):
    digits = '0123456789ABCDEF'
    if n < base:
        return digits[n]
    else:
        return toStr(n // base, base) + digits[n % base]


print(toStr(1438, 16))
print(toStr(1436, 10))

