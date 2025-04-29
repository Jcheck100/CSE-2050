def rrs(s):
    if len(s) <= 1:
        return s
    return rrs (s[1:]) + s[0]

print(rrs("hello"))
