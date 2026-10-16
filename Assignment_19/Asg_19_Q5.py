import MarvellousFMR_Q4
from functools import reduce

def isPrime(n):
    if (n<2):
        return False
    for i in range (2,n):
        if (n%i==0):
            return False
    return True

doubleNum=lambda no1:no1*2

maxno = lambda No1,No2: No1 if No1>No2 else No2

# def maxno(no1):
#     return max(no1)

def main():
    # numlist=list()
    # No1=int(input("Enter number of elements to be in list "))
    
    # for i in range(No1):
    #    No2=int(input("Enter elements to be in list "))
    #    numlist.append(No2)
    numlist= [2, 70 , 11, 10, 17, 23, 31, 77]
    print(numlist)
    FData=list(filter(isPrime,numlist))
    MData=list(map(doubleNum,FData))
    RData=reduce(maxno,MData)
    print("Data after filter :",FData)
    print("Data after map :",MData)
    print("Data after Reduce :",RData)
if __name__=="__main__":
  main()
