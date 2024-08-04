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

def calculate_speed(distance, time, unit="mph"):
  """Calculates speed in miles per hour (mph) or kilometers per hour (kph)."""
  if unit == "mph":
    speed = distance / time
  elif unit == "kph":
    speed = distance / time * 1.60934  # Convert miles to kilometers
  else:
    return "Invalid unit. Please enter 'mph' or 'kph'."
  return speed

print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Rectangle Area")
print("6. Circle Area")
print("7. Calculate Speed")

while True:
  # Take input from the user
  choice = input("Enter choice(1/2/3/4/5/6/7): ")

  # Check if choice is one of the seven options
  if choice in ('1', '2', '3', '4', '5', '6', '7'):
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
      elif choice == '4':
        print(num1, "/", num2, "=", divide(num1, num2))
    elif choice == '5':
      try:
        length = float(input("Enter the length: "))
        width = float(input("Enter the width: "))
      except ValueError:
        print("Invalid input. Please enter numbers only.")
      print("The area of the rectangle is:", rectangle_area(length, width))
    elif choice == '6':
      try:
        radius = float(input("Enter the radius: "))
      except ValueError:
        print("Invalid input. Please enter numbers only.")
      print("The area of the circle is:", circle_area(radius))
    elif choice == '7':
      try:
        distance = float(input("Enter the distance: "))
        time = float(input("Enter the time: "))
        unit = input("Enter the unit ('mph' or 'kph'): ")
      except ValueError:
        print("Invalid input. Please enter numbers only.")
      print("The speed is:", calculate_speed(distance, time, unit))
  else:
    print("Invalid input. Please enter a number between 1 and 7.")