import threading

def eventhread():
   print("Inside Even thread :",threading.get_ident())
   dolist=list()
   for i in range(2,22):
    if i%2==0:
     dolist.append(i)

   return dolist


def Oddthread():
   print("Inside Odd thread :",threading.get_ident())
   dolist=list()
   for i in range(2,22):
    if i%2!=0:
     dolist.append(i)

   return dolist

def main():
  print("Inside main thread :",threading.get_ident())
  print(f"list of even no is {eventhread()}")
  T1=threading.Thread(target=eventhread)
  T1.start()
  
  T2=threading.Thread(target=Oddthread)
  T2.start()
  print(f"list of Odd no is {Oddthread()}")
  

if __name__=="__main__":
    main()