#Included for calculation later on.
import math

#Output user will see when running the code.
print('''Choose either 'investment' or 'bond' from the menu below to proceed:

investment  - to calculate the amount of interest you'll earn on interest
bond        - to calculate the amount you'll have to pay on a home loan \n''')

#User to select INVESTMENT or BOND.  Character case does not matter.
choice1 = input("Please choose INVESTMENT or BOND: ")
choice1 = choice1.upper()

#If spelling is incorrect, program will display message and code will not run.
if(choice1 == "INVESTMENT")or(choice1 == "BOND"):
    print(f"You have chosen {choice1}.")
else:
    print("Your selection is invalid, please make sure your spelling is correct. Formulae will not calculate unless input is valid")


#If user chose INVESTMENT, user will be asked to input various numerical data.
#User will have to choose between SIMPLE and COMPOUND interest for calculation later on.  Spelling is important, character case does not matter.
if(choice1 == "INVESTMENT"):
    money = float(input("How much money are you depositing in rands? "))
    interest_rate = float(input("At what interest rate in percentage, only input number: "))
    interest_rate = interest_rate / 100
    years = float(input("How many years are you investing for? "))  
    interest = input("Please choose SIMPLE os COMPOUND: ")
    interest = interest.upper()

    #If spelling of SIMPLE or COMPOUND is incorrect, a message will output and code will not continue. 
    if(interest == "SIMPLE")or(interest == "COMPOUND"):
        print(f"You have chosen {interest}.")
    else:
        print("Your selection is invalid, please make sure spelling is correct. Formulae will not calculate unless input is valid")

    #Formula for SIMPLE and COMPOUND respectively.  Code will output result to user.  
    if(interest == "SIMPLE"):
        total_amount_simple = money * (1 + interest_rate * years)
        total_amount_simple = round(total_amount_simple)
        print(f"The total amount when SIMPLE interest is applied, is: R{total_amount_simple}")
    elif(interest == "COMPOUND"):
        total_amount_compound = money * math.pow((1 + interest_rate), years)
        total_amount_compound = round(total_amount_compound)
        print(f"The total amount when COMPOUND interest is applied, is: R{total_amount_compound}")


#If user chose BOND, user will be asked to input various numerical data.
#Formula to work out monthly repayment.  Code will output result to user.
elif(choice1 == "BOND"):
    value_house = float(input("The value of the house in rands (no spaces, eg: 10000): "))
    bond_interest_rate = float(input("At what interest rate in percentage, only input number: "))
    monthly_interest_rate = (bond_interest_rate/100)/12
    repayment_period = float(input("How many months will it take to repay the bond? "))
    repayment = (monthly_interest_rate * value_house)/(1 - (1 + monthly_interest_rate)**(-repayment_period))
    repayment = round(repayment)
    print(f"The total monthly repayment amount is: R{repayment}")

