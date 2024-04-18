#number tasks
def add_numbers() :

    number1 = input(float("Enter the first number. "))
    number2 =input(float("Enter the second number. "))

    sum = number1 + number2
    return number1 + number2

def perform_task(result) :
    if 10<= result <= 20:
        print("the sum is between 10 and 20.")
    elif result >100:
        print("The sum is greater than 100.")
    elif result <0:
        print("No negative numbers allowed.")
    else:
        print("The sum is:", result)

if "__ justin__"== "__main__":
    result = add_numbers()
    perform_task(result)



    
    










    
    
    


