keypad = {
    '0': ' ',
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz',
}


def read_key(keys, start):
    first_char = keys[start]

    max_len = 3
    if first_char in ['7', '9']:
        max_len = 4

    end = start
    for i in range(max_len):
        if (end < len(keys)) and (keys[end] == first_char):
            end += 1

    return end, keys[start:end]


def keypad_string(keys):
    '''
    Given a string consisting of 0-9,
    find the string that is created using
    a standard phone keypad
    | 1        | 2 (abc) | 3 (def)  |
    | 4 (ghi)  | 5 (jkl) | 6 (mno)  |
    | 7 (pqrs) | 8 (tuv) | 9 (wxyz) |
    |     *    | 0 ( )   |    #     |
    You can ignore 1, and 0 corresponds to space

    >>> keypad_string('12345')
    'adgj'

    >>> keypad_string('4433555555666')
    'hello'

    >>> keypad_string('2022')
    'a b'

    >>> keypad_string('')
    ''

    >>> keypad_string('111')
    ''
    '''

    if (len(keys) == 0):
        return ""

    i = 0
    output = ''

    while i < len(keys):
        i, next_key = read_key(keys, i)
        if next_key.startswith('1'):
            output += ""
        else:
            output += keypad[next_key[0]][len(next_key) - 1]

    return output
