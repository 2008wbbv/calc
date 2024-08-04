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
    return "

print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
while True:
  # Take input from the user
  choice = input("Enter choice(1/2/3/4): ")
  # Check if choice is one of the four options
  if choice in ('1', '2', '3', '4'):
    try:
      num1 = float(input("Enter first number: "))
      num2 = float(input("Enter second number: "))
    except ValueError:
      print("Invalid input. Please enter numbers only.")