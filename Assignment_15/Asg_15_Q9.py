from functools import reduce
Prodelements= lambda No1,No2: No1 * No2

def main():
 data=[2,2,4,10]
 Rdata=reduce(Prodelements,data)
 print(f"Prod of all elements is {data} is {Rdata}")
if __name__=="__main__":
 main()
