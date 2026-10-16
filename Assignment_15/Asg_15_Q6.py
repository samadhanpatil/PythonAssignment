from functools import reduce
Maxelements= lambda No1,No2: No1 if No1<No2 else No2

def main():
 data=[2,3,40000,5,6,34,1000,-2]
 Rdata=reduce(Maxelements,data)
 print(f"Minimum number from list {data} is {Rdata}")
if __name__=="__main__":
 main()
