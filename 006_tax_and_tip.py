# The program that you create for this exercise will begin by reading the cost of a meal
# ordered at a restaurant from the user. Then your program will compute the tax and
# tip for the meal. Use your local tax rate when computing the amount of tax owing.
# Compute the tip as 18 percent of the meal amount (without the tax). The output from
# your program should include the tax amount, the tip amount, and the grand total for
# the meal including both the tax and the tip. Format the output so that all of the values
# are displayed using two decimal places

def tax_and_tip(cost, tax_rate = 0.15, tip = 0.18):
  tax = cost * tax_rate
  tip = cost * tip
  grand_total = cost + tax + tip
  print(f"Tax Amount: ${tax:.2f}, Tip Amount:${tip:.2f}, Grand Total: ${grand_total:.2f}")


tax_and_tip(100)
tax_and_tip(20, 0.1, 0.2)
