def listdetails(data):
  sumno=0
  for i in range(len(data)):
    sumno=sumno+data[i]
   
  return sumno
def main():
    Elist=list()
    No1=int(input("Enter number of Elements "))

    for i in range(No1):
     No2=int(input(f"Enter element for list  "))
     Elist.append(No2)
    print("List elements are ",Elist)
    Ret =listdetails(Elist)
    print(f"Sum of element in list are :",Ret)
if __name__=="__main__":
 main()
