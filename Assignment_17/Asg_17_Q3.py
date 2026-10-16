def factno(no1):
  fact=1
  for i in range(1,no1+1):
   fact=fact*i
             
  return fact
def main():
 No1=int(input("Enter 1st number "))
 print("factoril of no is ",factno(No1))
if __name__=="__main__":
 main()
