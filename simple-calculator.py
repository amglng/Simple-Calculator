num_1 = int(input("Enter a number? "))
operator = (input("Choose a operator!(+, -, *, /)"))
num_2 = int(input("Enter a number? "))

def addition():
    add = num_1 + num_2
    return add

add = addition

def subtraction():
    minus = num_1 - num_2
    return minus

minus = subtraction

def multiplication():
    power = num_1 * num_2
    return power

power = multiplication

def division():
    divide = num_1 / num_2
    return divide

divide = division

print(addition())