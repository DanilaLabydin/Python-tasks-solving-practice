# Your task is to create a function that does four basic mathematical operations.
#The function should take three arguments - operation(string/char), value1(number), value2(number).
#The function should return result of numbers after applying the chosen operation.

# best practice
def basic_op(operator, value1, value2):
    return eval(f'{value1}{operator}{value2}')

print(bool(0 == 0.0))

operator = input('Enter an operator: ')
nb1 = input('Enter the first number: ')
nb2 = input('Enter the second number: ')

print(basic_op(operator, nb1, nb2))

