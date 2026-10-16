from multiprocessing import Pool
import time

def square(no):
  sumno1=0
  for i in range(1,no+1):
    sumno=i**2
    sumno1=sumno1+sumno
  return sumno1
def main():

  data=[1000000,2000000,3000000,4000000]
  print(f"Pass data list is {data}")
  # ret=square(data)
  
  start_time=time.perf_counter() 
  with Pool() as pool:
    ret=pool.map(square,data)
 
  print(f"results using pool is {ret}")
  # end_time=time.perf_counter()
  # print(f"Time required is {end_time-start_time:.4f}")

if __name__=="__main__":
  main()


 