def Sumoffactors(no1):
  Sumno=0
  for i in range(1, no1+1):
    if no1%i==0:
    #  print(f"{i} is factor of {no1}")
     Sumno=Sumno+i
                   
             
  return Sumno
def main():
 No1=int(input("Enter 1st number "))
 print("Sum of digit is ",Sumoffactors(No1))
if __name__=="__main__":
 main()
