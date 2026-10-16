def checkno():
 lst=list()
 for i in range(2,22):
   if i%2==0:
    lst.append(str(i))

 return ' '.join(lst) 
 

def main():
 
 print(f"list of 1st 10 even no is : {checkno()}")
       


if __name__=="__main__":
 main()
