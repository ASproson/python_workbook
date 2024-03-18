# Create a program that reads the length and width of a farmer’s field from the user in
# feet. Display the area of the field in acres

def area_of_field(length, width):
  area = length * width
  print(f"{area / 43560} acres")

area_of_field(100, 100)
area_of_field(240, 100)
area_of_field(24000, 10000)

