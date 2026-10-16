from functools import reduce
Evenlist= lambda No1: No1%2==0 

def main():
 data=[2,2,4,10,19,13]
 Rdata=list(filter(Evenlist,data))
 print(f"Prod of all elements is {data} is {Rdata}")
if __name__=="__main__":
 main()
