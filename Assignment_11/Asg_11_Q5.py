def palindrome(s):
   if s==s[::-1]:
     return True
   else:
     return False

def main():
  s= input("enter string")

  print("palindrome string is : ", palindrome(s))


if __name__=="__main__":
 main()

 