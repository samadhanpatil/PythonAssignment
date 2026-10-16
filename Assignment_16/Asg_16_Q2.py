def ChkNum(No1):
 if No1%2==0:
  return "Even Number"
 else:
  return "Odd Number"


def main():
 Ret=int(input("Enter String to Display "))
 
 print("Pass Number is  :",ChkNum(Ret))

if __name__=="__main__":
 main()
