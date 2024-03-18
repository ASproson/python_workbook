# In many jurisdictions a small deposit is added to drink containers to encourage people
# to recycle them. In one particular jurisdiction, drink containers holding one liter or
# less have a $0.10 deposit, and drink containers holding more than one liter have a
# $0.25 deposit.

# Write a program that reads the number of containers of each size from the user.
# Your program should continue by computing and displaying the refund that will be
# received for returning those containers. Format the output so that it includes a dollar
# sign and always displays exactly two decimal places.

def bottle_deposits(containers):
  small_deposit = 0.1
  large_deposit = 0.25
  refund = (containers["small"] * small_deposit) + (containers["large"] * large_deposit)
  print(f"Refund amount: ${refund:.2f}")

dictOne = { "small": 20, "large": 10}
dictTwo = { "small": 1, "large": 5}

bottle_deposits(dictOne)
bottle_deposits(dictTwo)
