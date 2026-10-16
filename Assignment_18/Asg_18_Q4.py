def listdetails(data,ElSearch):
  sumno=0
  for i in range(len(data)):
    if data[i]==ElSearch:
     print(f"Results is : {data[i]} --->{ElSearch}")
     sumno=sumno+1
  return sumno
def main():
    Elist=list()
    No1=int(input("Enter number of Elements "))

    for i in range(No1):
     No2=int(input(f"Enter element for list  "))
     Elist.append(No2)
    No3=int(input("Enter Elements to be Search"))
    
    print("List elements are ",Elist)
    Ret =listdetails(Elist,No3)
    print(f"Frequency of number in list is :",Ret)
if __name__=="__main__":
 main()
