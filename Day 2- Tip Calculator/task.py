print("Welcome to the tip calculator app!")
bill_amount = float(input("What was the total bill amount: $"))
tip = int(input("How much tip would you like to give? (in percentage): "))
no_of_people = int(input("How many people to split the bill? "))
total_tip = (tip / 100 * bill_amount)
total_amount = total_tip + bill_amount
split_bill = total_amount / no_of_people
round_split_bill = round(split_bill, 2)
print(f"The total tip is: ${total_tip}")
print(f"The total amount after the tip is: ${total_amount}")
print(f"Each person needs to pay: ${round_split_bill}")
