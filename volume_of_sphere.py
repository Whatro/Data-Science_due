import math 

def calculate_volume_of_sphere(radius):
  return (4/3) * math.pi * radius ** 3
radii_one = 30
radii_two = 40

first_calculation = calculate_volume_of_sphere(radii_one)
second_calculation = calculate_volume_of_sphere(radii_two)

print(first_calculation)
print(second_calculation)

git add volume_of_sphere.py
