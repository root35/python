from stack import Stack


def is_match(char1, char2):
    if char1 == '(' and char2 == ')':
        return True
    if char1 == '[' and char2 == ']':
        return True
    if char1 == '{' and char2 == '}':
        return True
    return False


def is_bracket_balanced(text: str):
    '''
    Check if brackets and parentheses are balanced.

    >>> is_bracket_balanced('{ }')
    True
    >>> is_bracket_balanced('{ } { }')
    True
    >>> is_bracket_balanced('( ( { [ ] } ) )')
    True

    >>> is_bracket_balanced('( ( )')
    False
    >>> is_bracket_balanced('{ { { ) } ]')
    False
    >>> is_bracket_balanced('[ ] [ ] ] ]')
    False

    >>> is_bracket_balanced(') }')
    False
    '''
    if len(text) == 0:
        return False

    stack = Stack()
    is_balanced = True

    for char in text:
        if char in '[({':
            stack.push(char)
        elif char in '])}':
            top = stack.pop()  # False if stack is empty
            if not top or not is_match(top, char):
                is_balanced = False
                break

    return stack.is_empty() and is_balanced is True


# Method:
#
# Iterate through the string and:
# - If opening parenthese/bracket:
#   - push it
# - If closing parenthese/bracket:
#   - pop the last character
#   - if it is an opening parenthese/bracket resp.
#     - continue
#   - else:
#     - stop -> unbalanced
#
# If we iterate over all characters in the string and stack is empty,
# then parentheses and brackets are balanced.
