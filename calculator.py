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

def mean(numbers):
    if not numbers:
        raise ValueError("Cannot calculate mean of empty list")
    return sum(numbers) / len(numbers)

def median(numbers):
    if not numbers:
        raise ValueError("Cannot calculate median of empty list")
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    if n % 2 == 1:
        return sorted_numbers[n//2]
    else:
        return (sorted_numbers[n//2 - 1] + sorted_numbers[n//2]) / 2

def mode(numbers):
    if not numbers:
        raise ValueError("Cannot calculate mode of empty list")
    from collections import Counter
    counts = Counter(numbers)
    max_count = max(counts.values())
    modes = [num for num, count in counts.items() if count == max_count]
    return modes[0] if len(modes) == 1 else modes

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def kilometers_to_miles(kilometers):
    return kilometers * 0.621371

def miles_to_kilometers(miles):
    return miles * 1.60934

def reverse_string(s):
    return s[::-1]

def capitalize_words(s):
    return ' '.join(word.capitalize() for word in s.split())

def count_characters(s):
    return len(s)

def count_words(s):
    return len(s.split())

def is_palindrome(s):
    s = s.lower().replace(' ', '')
    return s == s[::-1]

# Second test change for another branch
