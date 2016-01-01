def euclidGcd(a,b):
    if a%b==0:
        return b
    return euclidGcd(b,a%b)

def euclidLCM(a,b):
    print a*b,euclidGcd(a,b)
    return (a*b)/euclidGcd(a,b)

print euclidLCM(24,18)