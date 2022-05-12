"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, add_mult, add_cubes )


while True:
    user_input = input("Enter your equation: ")
    tokens = user_input.split(' ')
    num1=float(tokens[1])
    # num2=float(tokens[2])
    # num3=float(tokens[3])

    if len(tokens) >= 4:
        num3=float(tokens[3])
    if len(tokens) >= 3:
        num2=float(tokens[2])

    if "q" in tokens:
        break

    elif tokens[0]=='+':
        print(add(num1, num2))
    elif tokens[0] == '-':
        print(subtract(num1, num2))
    elif tokens[0]=='*':
        print(multiply(num1, num2))
    elif tokens[0] == '/':
        print(divide(num1, num2))
    elif tokens[0]=='square':
        print(square(num1))
    elif tokens[0] == 'cube':
        print(cube(num1))
    elif tokens[0]=='pow':
        print(power(num1, num2))
    elif tokens[0] == 'mod':
        print(mod(num1, num2))
    elif tokens[0]=='+*':
        print(add_mult(num1,num2,num3))
    elif tokens[0] == '+cube':
        print(add_cubes(num1, num2))
    else:
        print("invalid")

