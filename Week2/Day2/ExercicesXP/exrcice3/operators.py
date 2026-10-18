def addOperator(x, y):
    return x + y


def divideOperator(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y
