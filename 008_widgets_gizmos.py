# An online retailer sells two products: widgets and gizmos. 
# Each widget weighs 75 grams. 
# Each gizmo weighs 112 grams. 
# Write a program that reads the number of
# widgets and the number of gizmos in an order from the user. Then your program
# should compute and display the total weight of the order

def widgets_and_gizmos(order):
  widget_weight = 75 * order["widget"]
  gizmo_weight = 112 * order["gizmo"]
  total_weight_grams = widget_weight + gizmo_weight
  total_weight_kg = total_weight_grams / 1000
  print(f"Total weight of the order is {total_weight_kg}kg")


order_one = {"widget" : 100, "gizmo" : 25}
order_two = {"widget" : 17, "gizmo" : 0}
order_three = {"widget" : 1, "gizmo" : 0}


widgets_and_gizmos(order_one)
widgets_and_gizmos(order_two)
widgets_and_gizmos(order_three)



