import math

#First output that the user sees when the program runs, as stated by the task.
question = input("""Choose either 'investment' or 'bond' from the menu below to proceed:\n
investment -     to calculate the amount of interest you'll earn on your investment
bond -     to calculate the amount you'll have to pay on a home loan\n""")

#If user entered investments, the second set of questions will be asked.
if question.lower() == "investment":
    saving = int(input("What amount of money do you want to deposit: "))
    interest = int(input("Please enter the interest rate you would like to apply for: "))
    year = int(input("How many years would you like to have the loan out for? "))
    interest_type = input(" Would you like compound interest of simple interest ")

#User will be ask if they need a simple or compound interest rate to be applied on their investment.
    if interest_type.lower() == "simple":
        interest_rate = interest / 100
        payment_pcm = round((saving * (1 + interest_rate * year)), 2)
        print(payment_pcm)
    elif interest_type.lower() == "compound":
        interest_rate = interest / 100
        payment_pcm = round((saving * math.pow((1 + interest_rate), year)), 2)
        print(payment_pcm)

#If the user chooses bonds then the following questions and calculating will be applied.
elif question.lower() == "bond":
    house_price = int(input("Please enter your house price here: "))
    interest = int(input("Please enter the interest rate you would like to apply for: "))
    months = int(input("How many months would you like to have the loan out for? "))
    percentage_conversion = interest / 100
    interest_rate = percentage_conversion / 12
    payment_pcm = round(((interest_rate * house_price) / (1 - (1 + interest_rate) ** (-months))), 2)
    print(payment_pcm)
else:
    print("Please enter choose a valid response")
