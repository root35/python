
def count_capitals_in_file(filename):
    '''
    Count the number of capital letters in a file.

    >>> count_capitals_in_file('02_test_file.txt')
    39
    '''
    n_capitals = 0
    iterator = iter(open(filename))

    while True:
        try:
            line = next(iterator)
            for char in line:
                if char.isupper():
                    n_capitals += 1
        except StopIteration:
            break

    return n_capitals
