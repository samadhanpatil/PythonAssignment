from multiprocessing import Pool
import time
import os
import math

# def isPrime(n):
#     if (n<2):
#         return False
#     for i in range (2,n):
#         if (n%i==0):
#             return False
#     return True

# def ChkPrime(data1):
# #  cnt=0
#  result=list()
#  for x in data1:
#   cnt=0
#   for i in range(1,x+1):
#        if isPrime(i):
#         cnt=cnt+1   
#   result.append((cnt))
 
#  return result
# # ' '.join(result)
# #  print(total) 
def count_primes_up_to(n):
    """Counts the number of prime numbers between 1 and n (inclusive)."""
    if n < 2:
        return 0
    
    count = 0
    for num in range(2, n + 1):
        is_prime = True
        # Check divisibility up to the square root of the number
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            count += 1
            
    return count

def main():
 print(f"PID of Main {os.getpid()} PPID of Parent is {os.getppid()}")
 start_time=time.perf_counter() 
 data = [10000,20000,30000,40000]

 with Pool() as pool:
    ret=pool.map(count_primes_up_to,data)

 print(f"results using pool is {ret}")

 end_time=time.perf_counter()
 print(f"Time required is {end_time-start_time:.4f}")


if __name__=="__main__":
  main()


 