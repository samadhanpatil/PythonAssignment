from functools import reduce
Maxstring= lambda No1: len(No1)>5 

def main():
 data=['Bombay','Pune','Banglore','Delhi']
 Fdata=list(filter(Maxstring,data))
 print(f"Minimum number from list {data} is {Fdata}")
if __name__=="__main__":
 main()
