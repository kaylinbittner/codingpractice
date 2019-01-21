single_digits = list(range(0, 10))

print(single_digits)

squares = []

for digit in single_digits:
  print(digit)
  squares.append(digit*digit)
  
print(squares)

cubes = [cube**3 for cube in single_digits]

print(cubes)
