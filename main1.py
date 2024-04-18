import personal_finance

#Prompt the user for income sources and amounts

income_sources = {}

print("Enter your income sources and amounts (type 'done' to finish):")
while True:
    source = input("Source: ")
    if source == 'done':
         break
    amount = float(input("Amount: "))
    income_sources[source] = amount

#Calculate total income

total_income = personal_finance.calculate_income(income_sources)

#Prompt the user for expenses and their categories

expenses = {}

print("Enter your expenses, their categories, and amount (type 'done' to finish):")
while True:
     expense = input("Expense: ")
     if expense == 'done':
          break
     category = input("Category: ")
     amount = float(input("Amount: "))
     expenses[expense] = (category, amount)

#Categorized and calculate total expenses
     
categorized_expenses = personal_finance.categorize_expenses(expenses)
total_expenses = personal_finance.calculate_total_expense(categorized_expenses) 

#Calculate the balance

balance = personal_finance.calculate_balance(total_income, total_expenses)

#Display the user's financial information

print ("\nTotal Income:", total_income)
print("Categorized Expenses:", categorized_expenses)
print("Total Expenses:", total_expenses)
print("Net Balance:", balance)     


    