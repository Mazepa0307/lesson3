def calculate():
    num1 = float(input('Enter first number: '))
    operator = input('Enter operator: ')
    num2 = float(input('Enter second number: '))

    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 ==0:
            print('Cannot divide by zero')
            return None
        result = num1 / num2
    else:
        print('Invalid operator')
        return None
    return result
result = calculate()
if result is not None:
    print(f'The result is {result}')
