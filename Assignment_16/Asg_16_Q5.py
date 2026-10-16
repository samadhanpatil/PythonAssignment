
def main():
 lst1=list()
 for i in range(10,0,-1):
  lst1.append(str(i))

 return ' '.join(lst1)

if __name__=="__main__":
 
 print(f"return list is :", main())
