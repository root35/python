def find_sum(lst, n):
    """
    Function to find two number that add up to n
    :param lst: A list of integers
    :param n: The integer number n

    >>> lst = [1, 21, 3, 14, 80, 5, 60, 7, 6]
    >>> n = 81
    >>> print(find_sum(lst, n))
    [(1, 80), (21, 60)]
    """
    result = []
    i = 0
    while i < len(lst):
        j = i
        while j < len(lst):
            if (lst[i] + lst[j] == n):
                result.append((lst[i], lst[j]))
            j += 1
        i += 1
    return result
    # O(nlogn)




def binary_search_rec(data, key, index=0):
    '''
    >>> data = [1, 3, 5, 6, 7, 14, 21, 60, 80]
    >>> key = 1
    >>> binary_search_rec(data, key)
    0
    >>> key = 80
    >>> binary_search_rec(data, key)
    8
    >>> key = 5
    >>> binary_search_rec(data, key)
    2
    '''
    mid_index = len(data) // 2
    if mid_index >= len(data):
        return -1
    if key == data[mid_index]:
        return mid_index + index
    elif key < data[mid_index]:
        return binary_search_rec(data[:mid_index], key, index)
    else:
        index += mid_index + 1
        return binary_search_rec(data[mid_index+1:], key, index)

def find_sum_2(lst, n):
    '''
    Optimal solution

    >>> lst = [1, 21, 3, 14, 80, 5, 60, 7, 6]

    >>> n = 81
    >>> print(find_sum_2(lst, n))
    [(1, 80), (21, 60)]

    >>> n = 13
    >>> print(find_sum_2(lst, n))
    [(6, 7)]

    >>> n = 8
    >>> print(find_sum_2(lst, n))
    [(1, 7), (3, 5)]

    >>> lst = [8, 26, 75, 61, 63, 79]
    >>> n = 101
    >>> print(find_sum_2(lst, n))
    [(26, 75)]
    '''
    result = list()
    slst = sorted(list(set(lst)))
    i = 0
    while i < len(slst)-1:  # O(n)
        index = binary_search_rec(slst[i+1:], n - slst[i])  # O(logn)
        if index != -1:
            index += (i + 1)
            result.append((slst[i], slst[index]))
        i += 1
    return result
    # O(n logn)
