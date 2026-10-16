def checkperfectno(no1):
  cnt=0
  for i in range(1,no1):
    if no1%i==0:
     cnt=cnt+i

  if cnt==no1:
    return True
  else:
    return False

def main():
  no1=int(input("Enter number to check perfect or not"))
   
  print("Number is Perfect :", checkperfectno(no1))


if __name__=="__main__":
 main()
