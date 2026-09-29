amount_due = 50 # starting with the initial total price (50 cent)

# if the buyer owes money, keep repeating the acction inside this block
while amount_due > 0:
    print(f"Amount Due: {amount_due}")  # print how much money is still needed
    coin = int(input("Insert Coin: "))  # promt/ask the user for a coin and convert their answer to an inter
    if coin in [25, 10, 5]:     # check if the coin is valid
        amount_due = amount_due - coin  # subtract the valid coin value from what is owed

# once amount_due reaches 0 or less,the loop ends.
change_owed = abs(amount_due)   # calculate the remaining change (abs makes a negetive number positive)
print(f"Change Owed: {change_owed}")  # output the final change owed.
