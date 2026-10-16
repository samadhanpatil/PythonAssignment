import MarvellousFMR
from functools import reduce

def main():
    numlist=list()
    No1=int(input("Enter number of elements to be in list "))
    
    for i in range(No1):
       No2=int(input("Enter elements to be in list "))
       numlist.append(No2)
    # numlist=[4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70]
    print(numlist)
    FData=list(filter(MarvellousFMR.checkno,numlist))
    MData=list(map(MarvellousFMR.incrementno,FData))
    RData=reduce(MarvellousFMR.mult,MData)
    print("Data after filter :",FData)
    print("Data after map :",MData)
    print("Data after Reduce :",RData)
if __name__=="__main__":
  main()
