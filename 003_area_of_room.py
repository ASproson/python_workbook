# Write a program that asks the user to enter the width and length of a room. Once
# the values have been read, your program should compute and display the area of the
# room. The length and the width will be entered as floating point numbers. 

def area_of_room():
  error = "Please enter a number"

  while True:
    width = input("What is the width of the room?\n")
    try:
      width = float(width)
      break
    except ValueError:
      print(error)

  while True:
    length = input("What is the length of the room?\n")
    try:
      length = float(length)
      break
    except ValueError:
      print(error)
    
  print(f"The area of the room is {float(width) * float(length)}")

area_of_room()