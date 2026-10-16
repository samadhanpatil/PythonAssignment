import threading,time

def smalldetails(input):
   print("Inside smalldetails thread name :",threading.get_ident())
   print("Inside smalldetails thread :",threading.current_thread().name)
   cnt=0
   for i in input:
      if i.islower():
         cnt=cnt+1
   print("smalldetails list is :",cnt)         
   return cnt    
   
def Capdetails(input):
    
   print("Inside Capdetails thread name :",threading.get_ident())
   print("Inside Capdetails thread name :",threading.current_thread().name)
   cnt=0
   for i in input:
      if i.isupper():
         cnt=cnt+1
   print("Capdetails list is :",cnt)
   return cnt

def checkDigit(input):
   print("Inside checkDigit thread name :",threading.get_ident())
   print("Inside checkDigit thread :",threading.current_thread().name)
   cnt=0
   for i in input:
      if i.isdigit():
         cnt=cnt+1
   print("Digit list is :",cnt)
   return cnt

 

def main():
  print("Inside main thread :",threading.get_ident())
  Data="SamADHan3456"

  print("Original list is :",Data)
  start_time=time.perf_counter() 
  T1=threading.Thread(target=Capdetails,args=(Data,))
  T1.start()
  
  T2=threading.Thread(target=smalldetails,args=(Data,))
  T2.start()

  T3=threading.Thread(target=checkDigit,args=(Data,))
  T3.start()
  
  T1.join()
  T1.join()
  T3.join()
  end_time=time.perf_counter()
  print(f"Time required is {end_time-start_time:.4f}")

  # print(f"Results is Even list {EvenList(12)}")
  # print(f"Results is odd list {OddList(12)}")
if __name__=="__main__":
    main()