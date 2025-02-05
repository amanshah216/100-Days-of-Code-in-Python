from art import logo
print(logo)

# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary


username = input("What's your name: \n")
bid_amount = int(input("What's your bid: \n$"))

user_dict ={}
user_dict[username] = bid_amount

new_bids = input("Is there anyone else to bid? yes/no: \n")
