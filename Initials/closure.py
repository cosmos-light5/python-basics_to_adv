def power_raiser(x):
  def inner_value(y):
    return x**y
  return inner_value

square=power_raiser(2)
cube=power_raiser(3)

print(square(2))
print(cube(3))