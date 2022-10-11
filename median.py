"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""


while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break
print(numbers)


#Solution:
numbers.sort()
if len(numbers) % 2 == 0:
    a = numbers[len(numbers)//2]
    b = numbers[(len(numbers)//2)-1]
    c = ( a + b ) /2
    print(c)
if len(numbers) % 2 != 0:
    b = numbers[(len(numbers)//2)]
    print(b)
