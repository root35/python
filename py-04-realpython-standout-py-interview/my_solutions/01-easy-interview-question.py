from math import floor
from collections import Counter


def majority_element_indexes(lst):
    '''
    Return a list of the indexes of the majority element.
    Majority element is the element that appears more than
    floor(n / 2) times.
    If there is no majority element, return []

    >>> majority_element_indexes([1, 1, 2])
    [0, 1]

    >>> majority_element_indexes([1, 2, 3])
    []

    >>> majority_element_indexes([1])
    []

    >>> majority_element_indexes([1, 1, 1, 2, 2, 2])
    []

    >>> majority_element_indexes([1, 2, 1, 2, 2, 1, 0])
    []

    >>> majority_element_indexes([])
    []
    '''
    if len(lst) == 0 or len(lst) == 1:
        return []

    min_count = floor(len(lst) / 2)
    majority_element_indexes = list()
    uniq_elements = set(lst)

    for u_element in uniq_elements:  # time: O(uniq(n)) -> worst: 0(n)
        count = 0
        indexes = []

        for idx, element in enumerate(lst):  # time: O(n)
            if element == u_element:
                indexes.append(idx)
                count += 1

        if len(indexes) > min_count:
            majority_element_indexes.extend(indexes)

    return sorted(majority_element_indexes)  # O(n)


def majority_element_indexes_2(lst):
    '''
    Return a list of the indexes of the majority element.
    Majority element is the element that appears more than
    floor(n / 2) times.
    If there is no majority element, return []

    >>> majority_element_indexes_2([1, 1, 2])
    [0, 1]

    >>> majority_element_indexes_2([1, 2])
    []

    >>> majority_element_indexes_2([1, 2, 3])
    []

    >>> majority_element_indexes_2([1])
    []

    >>> majority_element_indexes_2([1, 1, 1, 2, 2, 2])
    []

    >>> majority_element_indexes_2([1, 2, 1, 2, 2, 1, 0])
    []

    >>> majority_element_indexes_2([])
    []
    '''
    if len(lst) == 0 or len(lst) == 1:
        return []

    min_count = floor(len(lst) / 2)
    majority_element_indexes = list()

    # Find the majority element
    counter = Counter(lst)
    max_count = max(counter.values())

    # Top element doesn't have majority count:
    if max_count <= min_count:
        return []

    # Found one or more majority elements:
    majority_element_indexes = [idx
                                for idx, value in enumerate(lst)
                                if counter[value] == max_count]

    return majority_element_indexes


def majority_element_indexes_3(lst):
    '''
    Return a list of the indexes of the majority element.
    Majority element is the element that appears more than
    floor(n / 2) times
    If there is no majority element, return []

    >>> majority_element_indexes_3([1, 1, 2])
    [0, 1]

    >>> majority_element_indexes_3([1, 2])
    []

    >>> majority_element_indexes_3([1])
    []

    >>> majority_element_indexes_3([])
    []
    '''
    if len(lst) == 0 or len(lst) == 1:
        return []

    min_count = floor(len(lst) / 2)

    # Find the majority element:
    counter = Counter(lst)
    max_element = counter.most_common(1)  # time: O(n)
    max_count = max_element[0][1]

    # No majority element:
    if max_count <= min_count:
        return []

    # One or more majority elements:
    return [idx
            for idx, element in enumerate(lst)
            if counter[element] == max_count]    # O(n)
