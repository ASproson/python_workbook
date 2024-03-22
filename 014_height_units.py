# Many people think about their height in feet and inches, even in some countries that
# primarily use the metric system. Write a program that reads a number of feet from
# the user, followed by a number of inches. Once these values are read, your program
# should compute and display the equivalent number of centimeters.
# Hint: One foot is 12 inches. One inch is 2.54 centimeters.

def height_units():
    error_msg = "Please enter a valid number"
    while True:
        try:
            feet = float(input("Please enter height in feet: \n"))
        except ValueError:
            print(error_msg)
        
        try:
            inches = float(input("Please enter remaining height in inches: \n"))
            break
        except ValueError:
            print(error_msg)
    
    total_inches = feet * 12 + inches
    convert_to_cm = total_inches * 2.54
    print(f"Converted height is: {convert_to_cm:.2f} centimeters")

height_units()
