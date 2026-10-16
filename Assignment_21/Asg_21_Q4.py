import threading,time
from queue import Queue
 
def Thread1(data1,result_queue):
   
  sumno=0
  for i in range(len(data1)):
    sumno=sumno+data1[i]
  
#   print(f"Reuslt of Thread-1 is ",sumno)
  result_queue.put(("Sum", sumno))


def Thread2(data1,result_queue):
   
  multno=1
  for i in range(len(data1)):
    multno=multno*data1[i]
   
#   print(f"Reuslt of Thread-2 is ",multno)
  result_queue.put(("Product", multno))


def main():
  data=list()
  # No1=int(input("Enter number of Elements "))

  # for i in range(No1):
  #   No2=int(input(f"Enter element for list  "))
  #   data.append(No2)
  data=[1,2,3,4,5]  
  print("Parent thread starts here",threading.get_ident())

  result_queue = Queue()
  start_time=time.perf_counter() 
  T1=threading.Thread(target=Thread1,args=(data,result_queue))
  T1.start()

  T1=threading.Thread(target=Thread2,args=(data,result_queue))
  T1.start()

  T1.join()
  T1.join()
  
    # Retrieve and display results from the main thread
  results = {}
  while not result_queue.empty():
        label, value = result_queue.get()
        results[label] = value

  print(f"Result from Thread 1: {results['Sum']}")
  print(f"Result from Thread 2: {results['Product']}")

#   print(f"Global variable values is {GlobalNo}")
  end_time=time.perf_counter()
  print(f"Time required is {end_time-start_time:.4f}")



if __name__=="__main__":
  main()


 