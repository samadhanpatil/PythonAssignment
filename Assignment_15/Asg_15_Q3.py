evenno=lambda no:no%2!=0
  
def main():
 data=[2,3,4,5,6]
 Fdata=list(filter(evenno,data))
 print(f"List of even number from list {data} is {Fdata}")
if __name__=="__main__":
 main()
