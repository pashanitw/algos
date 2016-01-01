__author__ = 'space'

def isPrime(number):
    print number
    if number!=2 & number>=2:
        x=number/2
        for i in range(2,x+1):
            if(number%i==0):
                devided=i
                print " is not prime number devided by"
                print devided
                break
            elif i==x:
                print " is a prime number"
    elif number<2:
         print "i is not a prime number"
    else :
        print "prime number"


isPrime(0)