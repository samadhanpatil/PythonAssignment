def reverseString(s):
    res = []
  
    # Traverse on s in backward direction
    # and add each character to the list
    for i in range(len(s) - 1, -1, -1):
        res.append(s[i])

    # Convert list back to string
    return ''.join(res)
def main():
  s= input("enter string")

  print("Reverse of nstringumber ", reverseString(s))


if __name__=="__main__":
 main()

#patil =,
#range(4, -1, -1)