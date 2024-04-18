number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))

#calculate the sum
sum = number1 + number2

#determine he output based on the sum
if sum < 0:
    print("No negative numbers")

elif 10 <= sum <=20:
    print("The sum is between 10 and 20.")

elif sum >100:
    print("The sum is above 100.")

else:
    print("The sum is "+ str(sum))