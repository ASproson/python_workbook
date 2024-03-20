# The surface of the Earth is curved, and the distance between degrees of longitude
# varies with latitude. As a result, finding the distance between two points on the surface
# of the Earth is more complicated than simply using the Pythagorean theorem.
# Let (t1, g1) and (t2, g2) be the latitude and longitude of two points on the Earth’s
# surface. The distance between these points, following the surface of the Earth, in
# kilometers is:
# distance = 6371.01 × arccos(sin(t1) × sin(t2) + cos(t1) × cos(t2) × cos(g1 − g2))
# The value 6371.01 in the previous equation wasn’t selected at random. It is
# the average radius of the Earth in kilometers.
# Create a program that allows the user to enter the latitude and longitude of two
# points on the Earth in degrees. Your program should display the distance between
# the points, following the surface of the earth, in kilometers.

# Hint: Python’s trigonometric functions operate in radians. As a result, you will
# need to convert the user’s input from degrees to radians before computing the
# distance with the formula discussed previously. The math module contains a
# function named radians which converts from degrees to radians.

import math

def distance_between_two_points(lat1, lon1, lat2, lon2):

  lat1 = math.radians(lat1)
  lat2 = math.radians(lat2)
  lon1 = math.radians(lon1)
  lon2 = math.radians(lon2)

  avg_radius_earth_km = 6371.01
  return  avg_radius_earth_km * math.acos(math.sin(lat1) * math.sin(lat2) + math.cos(lat1) * math.cos(lat2) * math.cos(lon1 - lon2))

new_york_lat = 40.7128
new_york_lon = -74.0060 

los_angeles_lat = 34.0522
los_angeles_lon = -118.2437

print(distance_between_two_points(new_york_lat, new_york_lon, los_angeles_lat, los_angeles_lon))
