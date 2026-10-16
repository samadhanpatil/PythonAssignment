def isPrime(n):
    if (n<2):
        return False
    for i in range (2,n):
        if (n%i==0):
            return False
    return True

def ChkPrime(data1):
 li = []
 for x in data1:
      if isPrime(x):
         li.append(x)

 total = 0
 for j in range(len(li)):
    total += li[j]
 return total
#  print(total) 
# if __name__=="__main__":
#  data = [13,5,45,7]
#  ret =ChkPrime(data)
#  print(ret)


# print(sumprimes([13,5,45,7,4,56,10,34,2,5,8]))
