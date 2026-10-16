def checkno(no1):
 if no1%5==0:
  return True
 else:
  return False
 

def main():
 no1=int(input("Enter Number to check "))
 print("Number is divisible by 5", checkno(no1))


if __name__=="__main__":
 main()
