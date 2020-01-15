import math


# Create a function called calc_dollars. In the function body, define a dictionary and store it in a variable named piggyBank. The dictionary should have the following keys defined.

# quarters
# nickels
# dimes
# pennies
# For each coin type, give yourself as many as you like.

def make_change():
    dollar_amount = 8.69
    piggy_bank = {
        "pennies": 0,
        "nickels": 0,
        "dimes": 0,
        "quarters": 0,
    }

# Once you have given yourself a large stash of coins in your piggybank, look at each key and perform the appropriate math on the integer value to determine how much money you have in dollars. Store that value in a variable named dollarAmount and print it.

    piggy_bank["quarters"] = math.floor(dollar_amount / .25)
    dollar_amount = dollar_amount % .25
    piggy_bank["dimes"] = math.floor(dollar_amount / .10)
    dollar_amount = dollar_amount % .10
    piggy_bank["nickels"] = math.floor(dollar_amount / .05)
    dollar_amount = dollar_amount % .05
    piggy_bank["pennies"] = math.ceil(dollar_amount / .01)
    dollar_amount = dollar_amount % .01

    return piggy_bank

print(make_change())

# **************ALTERNATE WAY TO SOLVE THIS*****************

# def fill_piggy_bank (dollarAmount):
#     quarters_quantity = 0
#     dimes_quantity = 0
#     nickels_quantity = 0
#     pennies_quantity = 0
#     while dollarAmount > .25:
#         dollarAmount -= .25
#         quarters_quantity += 1
#     while dollarAmount > .1:
#         dollarAmount -= .1
#         dimes_quantity += 1
#     while dollarAmount > .05:
#         dollarAmount -= .05
#         nickels_quantity += 1
#     while dollarAmount > .01:
#         dollarAmount -= .01
#         pennies_quantity += 1
#     piggyBank.update({
#         'quarters': quarters_quantity,
#         'dimes': dimes_quantity,
#         'nickels': nickels_quantity,
#         'pennies': pennies_quantity
#     })
#     print(piggyBank)
# fill_piggy_bank(dollarAmount)