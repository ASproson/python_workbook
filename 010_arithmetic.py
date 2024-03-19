# Create a program that reads two integers, a and b, from the user. Your program should
# compute and display:
# • The sum of a and b
# • The difference when b is subtracted from a
# • The product of a and b
# • The quotient when a is divided by b
# • The remainder when a is divided by b
# • The result of log10 a
# • The result of a^b (square)

import cmath

def arithmetic(a, b):
  sum = a + b
  diff = a - b
  product = a * b
  quotient = a / b
  remainder = a % b
  log10 = cmath.log10(a)
  squared = a ** b
  print(f"The sum of a + b is: {sum}")
  print(f"The difference of a - b is: {diff}")
  print(f"The product of a * b is: {product}")
  print(f"The quotient of a / b is: {quotient}")
  print(f"The remainder of a % b is: {remainder}")
  print(f"The log10 of a is: {log10}")
  print(f"The square of a ** b is: {squared} \n")


arithmetic(1, 1)
arithmetic(20, 2)