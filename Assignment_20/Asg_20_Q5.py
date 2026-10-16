import threading,time

def Thread1 (input1):
   print("Inside Thread1 name :",threading.get_ident())
   print("Inside Thread1 thread :",threading.current_thread().name)
   lst=list()
   for i in range(1,input1+1):
     lst.append(i)

   print("smalldetails list is :",''.join(str(lst)))         
   return ''.join(str(lst))    
   
def Thread2 (input1):
   print("Inside Thread2 name :",threading.get_ident())
   print("Inside Thread2   :",threading.current_thread().name)
   lst1=list()
   for i in range(input1,0,-1):
     lst1.append(i)

   print("Thread2 list is :",lst1)         
   return ''.join(str(lst1))    
   


def main():
  print("Inside main thread :",threading.get_ident())
  

#   print("Original list is :",Data)
  start_time=time.perf_counter() 
  T1=threading.Thread(target=Thread1,args=(50,))
  T1.start()
  
  T2=threading.Thread(target=Thread2,args=(50,))
  T2.start()


  T1.join()
  T1.join()
 
  end_time=time.perf_counter()
  print(f"Time required is {end_time-start_time:.4f}")

  # print(f"Results is Even list {EvenList(12)}")
  # print(f"Results is odd list {OddList(12)}")
if __name__=="__main__":
    main()