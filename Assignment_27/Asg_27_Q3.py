class Numbers():

  def __init__(self,No1):
    self.Value=No1

  def chkprime(self):
    if self.Value%2==0:
      return True
    else:
      return False

  def chkPerfect(self):
    if self.Value <= 0:
        return False
        
    sum_of_divisors = 0
    
    # Loop through all numbers from 1 up to num-1
    for i in range(1, self.Value):
        if self.Value % i == 0:
            sum_of_divisors += i
            
    # Return True if the sum equals the original number
    return sum_of_divisors == self.Value
  
  def factors(self):
    factors=list()
    for i in range(1,self.Value+1):
      if self.Value % i == 0:
        factors.append(str(i))

    return factors
  
  def SumFactors(self,lst):
    sumno=0
    for i in range(len(lst)):
      sumno=sumno+int(lst[i])
    
    return sumno


obj1=Numbers(24)
ret=obj1.chkprime()
print(f"Number is prime or not :- {ret}")
ret=obj1.chkPerfect()
print(f"Number is Perfect or not :- {ret}")
ret=obj1.factors()
print(f"Factors of number is  :- {ret}")
ret1=obj1.SumFactors(ret)
print(f"Sum of Factors of number is  :- {ret1}")


obj2=Numbers(12)
ret=obj2.chkprime()
print(f"Number is prime or not :- {ret}")
ret=obj2.chkPerfect()
print(f"Number is Perfect or not :- {ret}")
ret=obj2.factors()
print(f"Factors of number is  :- {ret}")
ret1=obj2.SumFactors(ret)
print(f"Sum of Factors of number is  :- {ret1}")
