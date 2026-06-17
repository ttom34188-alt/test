def add(a, b):
    # Testing polling trigger - new modification at 13:21
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def power(a, b):
    return a ** b

def modulo(a, b):
    if b == 0:
        raise ValueError("Cannot modulo by zero")
    return a % b

def logarithm(a, base=10):
    if a <= 0:
        raise ValueError("Cannot calculate logarithm of non-positive number")
    if base <= 0 or base == 1:
        raise ValueError("Base must be positive and not equal to 1")
    import math
    return math.log(a, base)

def sin(a):
    import math
    return math.sin(a)

def cos(a):
    import math
    return math.cos(a)

def tan(a):
    import math
    return math.tan(a)
