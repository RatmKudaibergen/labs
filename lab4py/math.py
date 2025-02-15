import math

def convert_to_rad(degree):
  return degree / 180 * math.pi


def trap_area(height, base1, base2):
  return height * (base1 + base2) / 2


def regpol_area(sides, side_len):
  apophem =  side_len / (2 * math.tan(convert_to_rad(180 / sides)))
  return round(sides * side_len * apophem / 2, 5)


def paral_area(base, height):
  return base * height


print(trap_area(5, 5, 6))
print(regpol_area(4, 25))
print(paral_area(5, 6))
