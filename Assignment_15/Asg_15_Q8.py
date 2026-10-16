from functools import reduce
DivNumber= lambda No1: (No1%3==0 and No1%5==0 )
def main():
 data=[2,3,4,5,13,15,35,90,60,120]
 Fdata=list(filter(DivNumber,data))
 print(f"Divisible by 3 and 5 are  {data} is {Fdata}")
if __name__=="__main__":
 main()
