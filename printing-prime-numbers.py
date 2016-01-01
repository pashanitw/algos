__author__ = 'space'

def printPrimeNumber(high):
    total=[True]*(high+1)
    total[0]=False
    total[1]=False
    print total
    for k in range(2,high+1):
        i=2
        while i*k<=high:
            total[i*k]=False
            i+=1

        if total[k]:
            print k
    print total

printPrimeNumber(2238)