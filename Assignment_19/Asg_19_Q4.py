import MarvellousFMR_Q4
from functools import reduce

def main():
    # numlist=list()
    # No1=int(input("Enter number of elements to be in list "))
    
    # for i in range(No1):
    #    No2=int(input("Enter elements to be in list "))
    #    numlist.append(No2)
    numlist= [5, 2, 3, 4, 3, 4, 1, 2, 8, 10]
    print(numlist)
    FData=list(filter(MarvellousFMR_Q4.checkno,numlist))
    MData=list(map(MarvellousFMR_Q4.MakeSquare,FData))
    RData=reduce(MarvellousFMR_Q4.addition,MData)
    print("Data after filter :",FData)
    print("Data after map :",MData)
    print("Data after Reduce :",RData)
if __name__=="__main__":
  main()
