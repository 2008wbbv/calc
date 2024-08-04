def add(x, y):
  """Adds two numbers together."""
  return x + y

def subtract(x, y):
  """Subtracts two numbers."""
  return x - y

def multiply(x, y):
  """Multiplies two numbers."""
  return x * y

def divide(x, y):
  """Divides two numbers."""
  if y == 0:
    return "Division by zero is not allowed"
  else:
    return x / y

def rectangle_area(length, width):
  """Calculates the area of a rectangle."""
  return length * width

def circle_area(radius):
  """Calculates the area of a circle."""
  from math import pi
  return pi * radius**2

print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Rectangle Area")
print("6. Circle Area")

while True:
  # Take input from the user
  choice = input("Enter choice(1/2/3/4/5/6): ")

  # Check if choice is one of the six options
  if choice in ('1', '2', '3', '4', '5', '6'):
    if choice in ('1', '2', '3', '4'):
      try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
      except ValueError:
        print("Invalid input. Please enter numbers only.")
      if choice == '1':
        print(num1, "+", num2, "=", add(num1, num2))
      elif choice == '2':
        print(num1, "-", num2, "=", subtract(num1, num2))
      elif choice == '3':
        print(num1, "*", num2, "=", multiply(num1, num2))