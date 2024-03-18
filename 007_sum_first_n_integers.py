# Write a program that reads a positive integer, n, from the user and then displays the
# sum of all of the integers from 1 to n

def sum_first_n_ints(n):
  sum = 0
  for i in range(1, n + 1):
    sum += i
  print(sum)

sum_first_n_ints(10)
sum_first_n_ints(25)

