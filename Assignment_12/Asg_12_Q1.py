def checkvowel(val1):
  
   for i in val1:
     if i in ['a','e','i','o','u','A','E','I','O','U']:
       return True
     else:
       return False

def main():
  no1=input("Enter character to check if it is vowel ")
  print("Character is vowel :- ", checkvowel(no1))


if __name__=="__main__":
 main()
