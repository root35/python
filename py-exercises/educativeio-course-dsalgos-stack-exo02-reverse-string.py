from stack import Stack


def reverse_string(text: str):
    '''
    >>> reverse_string('Salut')
    'tulaS'
    >>> reverse_string('')
    ''
    '''
    if len(text) == 0:
        return ''

    stack = Stack()

    for char in text:
        stack.push(char)

    reversed_str = ''
    while not stack.is_empty():
        reversed_str += stack.pop()

    return reversed_str
