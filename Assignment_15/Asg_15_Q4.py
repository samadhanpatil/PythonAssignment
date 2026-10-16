from functools import reduce
Addelements= lambda No1,No2: No1+No2

def main():
 data=[2,3,4,5,6]
 Rdata=reduce(Addelements,data)
 print(f"List of even number from list {data} is {Rdata}")
if __name__=="__main__":
 main()
