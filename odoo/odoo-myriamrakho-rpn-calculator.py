from collections import deque
from math import sqrt


operations = {'+': lambda x, y: y + x,
              '-': lambda x, y: y - x,
              '*': lambda x, y: y * x,
              '/': lambda x, y: y / x,
              'sqrt': lambda x: sqrt(x) }


def calculate(operator, arg1, arg2=None):
    if operator == 'sqrt':
        return operations[operator](arg1)
    else:
        return operations[operator](arg1, arg2)


def rpn_calculator(expression: str):
    arguments = expression.split(' ')
    queue = deque()

    for arg in arguments:
        if arg in operations:
            arg1 = float(queue.pop())
            arg2 = None
            if arg != 'sqrt':
                arg2 = float(queue.pop())
            current_result = calculate(arg, arg1, arg2)
            queue.append(current_result)
        else:
            queue.append(arg)

    return queue.pop()


def main():
    expression = input()
    result = rpn_calculator(expression)
    print(f'Input: {expression} - Result: {result}')


if __name__ == '__main__':
    main()
