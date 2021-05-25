from stack import Stack


def convert_int_to_binary(n: int):
    '''
    >>> convert_int_to_binary(242)
    '11110010'
    >>> convert_int_to_binary(1)
    '1'
    >>> convert_int_to_binary(2)
    '10'
    >>> convert_int_to_binary(101)
    '1100101'
    >>> convert_int_to_binary(13)
    '1101'
    >>> convert_int_to_binary(-10)
    '-1010'
    '''
    stack = Stack()
    stopval = abs(n)
    remainder = abs(n)

    while stopval > 0:
        remainder = stopval % 2
        stopval = stopval // 2
        stack.push(remainder)

    binary = ''
    if n < 0:
        binary += '-'
    while not stack.is_empty():
        binary += str(stack.pop())

    return binary
