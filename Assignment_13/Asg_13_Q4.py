def checkbinaryequivalent(no1):
   return bin(no1)
   
def main():
  no1=int(input("Enter number to get binary equivalent "))
   
  print(f"Binary equivalent of number {no1} : {checkbinaryequivalent(no1)}")


if __name__=="__main__":
 main()
