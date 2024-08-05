import math

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
  return math.pi * radius**2

def calculate_speed(distance, time, unit="mph"):
  """Calculates speed in miles per hour (mph) or kilometers per hour (kph)."""
  if unit == "mph":
    speed = distance / time
  elif unit == "kph":
    speed = distance / time * 1.60934  # Convert miles to kilometers
  else:
    return "Invalid unit. Please enter 'mph' or 'kph'."
  return speed

def calculate_exponential_sequence(base, exponent):
  """Calculates a sequence of numbers raised to increasing exponents."""
  result = []
  for i in range(exponent + 1):
    result.append(base**i)
  return result

def sin(angle):
  """Calculates the sine of an angle in radians."""
  return math.sin(math.radians(angle))

def cos(angle):
  """Calculates the cosine of an angle in radians."""
  return math.cos(math.radians(angle))

def tan(angle):
  """Calculates the tangent of an angle in radians."""
  return math.tan(math.radians(angle))

def log(base, x):
  """Calculates the logarithm of x to the base."""
  if base <= 0 or base == 1 or x <= 0:
    return "Invalid input. Base must be greater than 0 and not equal to 1, and x must be greater than 0."
  else:
    return math.log(x, base)

def factorial(n):
  """Calculates the factorial of n."""
  if n < 0:
    return "Factorial is not defined for negative numbers."
  elif n == 0:
    return 1
  else:
    return n * factorial(n - 1)

def square_root(x):
  """Calculates the square root of x."""
  if x < 0:
    return "Square root is not defined for negative numbers."
  else:
    return math.sqrt(x)

def cube_root(x):
  """Calculates the cube root of x."""
  return x**(1/3)

def absolute_value(x):
  """Calculates the absolute value of x."""
  return abs(x)

def power(base, exponent):
  """Calculates base raised to the exponent."""
  return base**exponent

def calculate_average(numbers):
  """Calculates the average of a list of numbers."""
  if not numbers:
    return "Cannot calculate average of an empty list."
  total = sum(numbers)
  average = total / len(numbers)
  return average

def calculate_sum(numbers):
  """Calculates the sum of a list of numbers."""
  if not numbers:
    return "Cannot calculate sum of an empty list."
  total = sum(numbers)
  return total

def calculate_variance(numbers):
  """Calculates the variance of a list of numbers."""
  if len(numbers) < 2:
    return "Variance cannot be calculated for less than two numbers."
  mean = calculate_average(numbers)
  variance = sum((x - mean)**2 for x in numbers) / (len(numbers) - 1)
  return variance

def calculate_standard_deviation(numbers):
  """Calculates the standard deviation of a list of numbers."""
  variance = calculate_variance(numbers)
  return math.sqrt(variance)

print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Rectangle Area")
print("6. Circle Area")
print("7. Calculate Speed")
print("8. Exponential Sequence")
print("9. Sine (sin)")
print("10. Cosine (cos)")
print("11. Tangent (tan)")
print("12. Logarithm (log)")
print("13. Factorial")
print("14. Square Root")
print("15. Cube Root")
print("16. Absolute Value")
print("17. Power")
print("18. Average")
print("19. Sum")
print("20. Variance")
print("21. Standard Deviation")

while True:
  # Take input from the user
  choice = input("Enter choice(1/2/3/4/5/6/7/8/9/10/11/12/13/14/15/16/17/18/19/20/21): ")

  # Check if choice is one of the twenty-one options
  if choice in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21'):
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
    elif choice == '8':
      try:
        base = float(input("Enter the base: "))
        exponent = int(input("Enter the exponent: "))
      except ValueError:
        print("Invalid input. Please enter numbers only.")
      sequence = calculate_exponential_sequence(base, exponent)
      print("Exponential sequence:", sequence)
    elif choice == '9':
      try:
        angle = float(input("Enter the angle in degrees: "))
      except ValueError:
        print("Invalid input. Please enter a number only.")
      print("The sine of", angle, "degrees is:", sin(angle))
    elif choice == '10':
      try:
        angle = float(input("Enter the angle in degrees: "))
      except ValueError:
        print("Invalid input. Please enter a number only.")
      print("The cosine of", angle, "degrees is:", cos(angle))
    elif choice == '11':
      try:
        angle = float(input("Enter the angle in degrees: "))
      except ValueError:
        print("Invalid input. Please enter a number only.")
      print("The tangent of", angle, "degrees is:", tan(angle))
    elif choice == '12':
      try:
        base = float(input("Enter the base: "))
        x = float(input("Enter the number: "))
      except ValueError:
        print("Invalid input. Please enter numbers only.")
      print("The logarithm of", x, "to the base", base, "is:", log(base, x))
    elif choice == '13':
      try:
        n = int(input("Enter a non-negative integer: "))
      except ValueError:
        print("Invalid input. Please enter a non-negative integer.")
      print("The factorial of", n, "is:", factorial(n))
    elif choice == '14':
      try:
        x = float(input("Enter a number: "))
      except ValueError:
        print("Invalid input. Please enter a number only.")
      print("The square root of", x, "is:", square_root(x))
    elif choice == '15':
      try:
        x = float(input("Enter a number: "))
      except ValueError:
        print("Invalid input. Please enter a number only.")
      print("The cube root of", x, "is:", cube_root(x))
    elif choice == '16':
      try:
        x = float(input("Enter a number: "))
      except ValueError:
        print("Invalid input. Please enter a number only.")
      print("The absolute value of", x, "is:", absolute_value(x))
    elif choice == '17':
      try:
        base = float(input("Enter the base: "))
        exponent = float(input("Enter the exponent: "))
      except ValueError:
        print("Invalid input. Please enter numbers only.")
      print(base, "raised to the power of", exponent, "is:", power(base, exponent))
    elif choice == '18':
      try:
        numbers = [float(x) for x in input("Enter numbers separated by spaces: ").split()]
      except ValueError:
        print("Invalid input. Please enter numbers only.")
      print("The average of the numbers is:", calculate_average(numbers))
    elif choice == '19':
      try:
        numbers = [float(x) for x in input("Enter numbers separated by spaces: ").split()]
      except ValueError:
        print("Invalid input. Please enter numbers only.")
      print("The sum of the numbers is:", calculate_sum(numbers))
    elif choice == '20':
      try:
        numbers = [float(x) for x in input("Enter numbers separated by spaces: ").split()]
      except ValueError:
        print("Invalid input. Please enter numbers only.")
      print("The variance of the numbers is:", calculate_variance(numbers))
    elif choice == '21':
      try:
        numbers = [float(x) for x in input("Enter numbers separated by spaces: ").split()]
      except ValueError:
        print("Invalid input. Please enter numbers only.")
      print("The standard deviation of the numbers is:", calculate_standard_deviation(numbers))
  else:
    print("Invalid input. Please enter a number between 1 and 21.")

elif choice == '18':
try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
except ValueError:
    print("Invalid input. Please enter integers only.")
print("The GCD of", num1, "and", num2, "is:", gcd(num1, num2))
