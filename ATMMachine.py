#ATM Machine
initial_balance = 1000000
withdraw_amount = input("Enter amount to with draw :")
withdraw_amount = int(withdraw_amount)

#check available balance
if(withdraw_amount <= initial_balance and withdraw_amount >= 5000) :
     
    #logic for withdrawing
    final_balance = initial_balance - withdraw_amount
    print(f"you have witdrawn {withdraw_amount} and your balance is {final_balance}.")
else:
    print("you have insufficient balance")