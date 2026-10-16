import threading,time
 
# Shared variable
counter = 0

# Lock object
lock = threading.Lock()

# Number of increments per thread
INCREMENTS = 10 

# Function executed by each thread
def increment_counter():
    global counter

    for i in range(INCREMENTS):
        # Acquire lock before updating shared variable
         with lock:
            counter += 1

# Create threads
threads = []
num_threads = 100000

for i in range(num_threads):
    thread = threading.Thread(target=increment_counter, name=f"Thread-{i+1}")
    threads.append(thread)
    thread.start()

# Wait for all threads to complete
# for thread in threads:
#     thread.join()

# Display final counter value
print("Expected Counter Value:", num_threads * INCREMENTS)
print("Final Counter Value   :", counter)

# def main():
#   data=list()
#   # No1=int(input("Enter number of Elements "))

#   # for i in range(No1):
#   #   No2=int(input(f"Enter element for list  "))
#   #   data.append(No2)
#   # # data=[2,34,5,67,89]
#   print("Parent thread starts here",threading.get_ident())

#   start_time=time.perf_counter() 
#   T1=threading.Thread(target=Thread1,args=(10))
#   T1.start()

#   T1=threading.Thread(target=Thread2,args=(6))
#   T1.start()

#   T1.join()
#   T1.join()
  
#   print(f"Global variable values is {GlobalNo}")
#   end_time=time.perf_counter()
#   print(f"Time required is {end_time-start_time:.4f}")

#   # print(f"Result Min",Minelement(data))
#   # print(f"Result Max ",Maxelement(data))

# if __name__=="__main__":
#   main()


 