# def PrintPattern(no1):
     
def main():
 No1=int(input("Enter 1st number "))
 for i in range(1,No1+1,1):
  if i!=1:
   print("\n")
  for i in range(1,No1+1,1):
   print(i, end=" ")
if __name__=="__main__":
 main()
