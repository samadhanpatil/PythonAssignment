class BankAccount():
  ROI=10.5

  def __init__(self,Name,Amt):
   self.name=Name
   self.Amount=Amt


  def Display(self):
    print(f"Account holder {self.name} is having current balance {self.Amount} ")

  
  def Deposit(self,DAmount):
    self.Amount=self.Amount+DAmount
    return self.Amount 

  def Withdraw(self,WAmount):
    if self.Amount>0 and self.Amount>=WAmount:
      # print(f"Total balance before Withdraw is {self.Amount}")
      WDAmt=self.Amount-WAmount
      self.Amount=WDAmt
      return WDAmt
    else:
      return -1

  def CalculateInterest(self):
    print(f"Total balance before Calculate Interest is {self.Amount}")
    Interest = (self.Amount * BankAccount.ROI) / 100
    return Interest

Obj1=BankAccount('Tony',1000)
Obj1.Display()
DepositAmt=Obj1.Deposit(50)
print(f"Total balance after deposit is {DepositAmt}")
WithdrawAmt=Obj1.Withdraw(99)
if WithdrawAmt ==-1:
 print(f"Insufficient Balance!!")
else:
  print(f"Total balance after Withdraw is {WithdrawAmt}")

CalculateInterestAmt=Obj1.CalculateInterest()
print(f"Total Calculated Interest is {CalculateInterestAmt}")

def main():

  Obj2=BankAccount('RD Burman',50000)
  Obj2.Display()
  DepositAmt=Obj2.Deposit(1000)
  print(f"Total balance after deposit is {DepositAmt}")
  WithdrawAmt=Obj2.Withdraw(20000)
  if WithdrawAmt ==-1:
   print(f"Insufficient Balance!!")
  else:
    print(f"Total balance after Withdraw is {WithdrawAmt}")

  CalculateInterestAmt=Obj2.CalculateInterest()
  print(f"Total Calculated Interest is {CalculateInterestAmt}")


if __name__=='__main__':
  main()