
def evens_up_to(ceiling):
    '''
    >>> evens = evens_up_to(8)
    >>> type(evens)
    <class 'generator'>
    >>> for even in evens:
    ...     print(even)
    2
    4
    6
    8
    THE END!

    '''

    num = 2
    while num <= ceiling:
        yield num
        num += 2
    yield 'THE END!'


if __name__ == '__main__':
    import doctest
    count, _ = doctest.testmod()
    print(count)
    if count == 0:
        print('*** ALL TESTS PASS ***\nGive someone a HIGH FIVE!')


# -- USAGE: python3 -m doctest test-with-doctest.py
#   -v: verbose option
# SEE: More info about 'python -m doctest'
