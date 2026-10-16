squareno=lambda no: no*no

def main():
 Data=[2,3,4,5]
 Mdata=list(map(squareno,Data))
 print("Square of number using map",Mdata)

if __name__=="__main__":
 main()
