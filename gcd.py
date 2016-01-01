def simpleGcd(a,b):
    gcd=1
    minVal=min(a,b)
    for i in range (minVal,0,-1):
        if (a%i==0)&(b%i==0):
            gcd=i
            break
    return gcd

print simpleGcd(10,6)
print simpleGcd(24,18)
print simpleGcd(5,2)
