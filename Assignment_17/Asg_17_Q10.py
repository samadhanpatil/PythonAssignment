def countno(No1):
 count=0
 for i in range(0,len(No1)):  
  count=count+int(No1[i])

 return count
def main():
 No1=(input("Enter number "))
 print(f"Total Digit in number is {countno(No1)}")
if __name__=="__main__":
 main()
