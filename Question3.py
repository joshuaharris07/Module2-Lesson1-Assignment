#Arithmetic Operations in Daily Life

#Task 1: Grocery Store Math 
# Calculate the total cost of three items you'd commonly find in a grocery store, given their individual prices. 
# For example, what would be the cost of bread, peanut butter, and jelly be?

item1_name = "bread"
item1_price = 1.49

item2_name = "peanut butter"
item2_price = 3.80

item3_name = "jelly"
item3_price = 2.05

total_price = item1_price + item2_price + item3_price
print(f"The total price of {item1_name}, {item2_name}, and {item3_name} is ${total_price}.")



# Task 2: Bank Interest 
# If you have a savings account with a particular initial amount and a fixed yearly interest rate, 
# calculate the total amount in your account after a year. 
# So if you had $10,000 at a 7% interest write code that would tell us the amount at the end of the year. 
# For the example the expected outcome would be $10,700.

initial_savings = float(input("Please enter the amount you currenty have in your savings: $"))
interest_rate = float(input("Please enter your fixed interest rate: "))
interest_decimal = interest_rate / 100

year_end_savings = initial_savings * (1 + interest_decimal)

print(f"Starting with ${initial_savings} and a {interest_rate}% interest rate, at the end of the year you will hav ${year_end_savings:.2f}.")