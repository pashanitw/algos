def euclidGcd(a,b):
    print a,b
    if a%b==0:
        return b
    return euclidGcd(b,a%b)

print euclidGcd(24,18)