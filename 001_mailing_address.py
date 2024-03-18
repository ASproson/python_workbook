# Create a program that displays your name and mailing address formatted in the manner you would see it on the outside of an envelope. You do not need to read any input from the user

def mailing_address():
  name = "John Smith"
  street = "000 Python Drive"
  city = "Pythonia"
  zipcode = "010 000"
  print(f"{name}\n{street}\n{city}\n{zipcode}")

mailing_address()