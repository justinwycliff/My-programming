"""Calculate total income from various sources."""

def calculate_income(income_sources):
    total_income = sum(income_sources.values())
    return total_income 


def categorize_expenses(expenses):

    """Categorize expenses into categories."""
    categorized = {}

    for expense, (category, amount) in expenses.items():
        if category in categorized:
            categorized[category].append((expense, amount))

        else:
            categorized[category] = [(expense, amount)]
    return categorized

def calculate_total_expense(categorized_expenses):

    """Calculate total expenditure."""
    total = 0
    for category, expenses in categorized_expenses.items():
        for _, amount in expenses:
            total += amount
    return total

def calculate_balance(income, expenses):
    
    """Calculate net balance."""
    return income - expenses











    




        











































