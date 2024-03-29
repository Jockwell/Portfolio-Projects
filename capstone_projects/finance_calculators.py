'''This program helps the user calculate the amount of interest or 
investment gain on their finances. '''
import math

def validate_calculator_type():
    '''Function to validate user's calculator choice type.'''
    while True:
        calculator_type = input("Enter either 'investment' or 'bond' from the menu above to proceed: ")
        calculator_type = str.lower(calculator_type)
        if calculator_type in ['investment', 'bond']:
            return calculator_type
        print("Please choose either 'investment' or 'bond'.")

# The user must choose between the 'investment' calculator or the 'bond' calculator.
print("\n")
print("Investment \t - To calculate the amount of interest you'll earn on your investment.")
print("Bond \t\t - To calculate the amount you'll have to pay on a home loan. \n\n")

USER_CHOICE = validate_calculator_type()

# Below is the code for when the user chooses investment.
if USER_CHOICE == "investment":
    print("You have selected the 'investment' calculator!")
    user_amount = float(input("Please enter the amount of money you are depositing (£):"))
    interest_rate = float(input("Please enter the interest rate for your investment (%):"))
    investment_term = float(input("Please enter the number of years you plan to invest:"))
    interest = input("Please choose between 'simple' & 'compound' interest:")
    INTEREST = str.lower(interest)


# Below is the code to calculate the 'simple interest investment' and prints the output.
    if INTEREST == "simple":
        simple_interest_total = user_amount * (1 + (interest_rate / 100) * investment_term)
        simple_investment_output = f'''Depositing £{user_amount} with the interest rate of 
        {interest_rate}%
        means the total amount once interest is applied will be £{round(simple_interest_total , 2)}
        after the {investment_term} year period.'''
        print('\u2500' * 50 + "\n\n" + simple_investment_output + "\n")
        print("This means the overall profit from your investment will be £" +
              str(round(simple_interest_total- user_amount, 2)) + ".\n")
        print('\u2500' * 50)

# Below is the code to calculate the 'compound interest investment' and prints the output.
    elif INTEREST == "compound":
        compound_interest_total = user_amount * math.pow(1 + (interest_rate /100), investment_term)
        compound_investment_output = f'''Depositing £{user_amount} 
        with the interest rate of {interest_rate}%
        means the total amount once interest is applied is £{round(compound_interest_total , 2)}
        after the {investment_term} year period.'''
        print('\u2500' * 50 + "\n\n" + compound_investment_output + "\n")
        print("This means the overall profit from your investment will be £" +
              str(round(compound_interest_total - user_amount , 2)) + ".\n")
        print('\u2500' * 50)
    else:
        print('\u2500' * 50)
        print("\n" + '''You have incorrectly chosen the type of the interest you want applied. 
              Please re-run the program enter either 'simple' or 'compound' 
              when requested in the 'Investment' calculator. \n''')
        print('\u2500' * 50)

# Below is the code for when the user decides to use the 'bond' calculator.
elif USER_CHOICE == "bond":
    print("You have selected the 'bond' calculator!")
    house_value = float(input("Please enter the present value of your house (£):"))
    bond_interest = float(input("Please enter the interest rate (%):"))
    monthly_interest = bond_interest / 100 / 12
    repayment_months = int(input("Please enter the months you plan to repay back this bond:"))
    repayment_total = (monthly_interest * house_value)/(1 -
                    (1 + monthly_interest) ** (-repayment_months))
    repayment_total = round(repayment_total, 2)
    bond_repayment_output = f'''If your house is valued at £{house_value}, 
    your interest rate is {bond_interest}%
    and you plan to repay your house off in {repayment_months} months.
    You will have to pay back £{repayment_total} each month.'''
    print('\u2500' * 50 + "\n\n" + bond_repayment_output + "\n\n" + '\u2500' * 50)
