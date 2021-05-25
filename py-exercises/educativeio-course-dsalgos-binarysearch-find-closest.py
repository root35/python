def find_closest(data, key, diff=0):
    if data is None or len(data) == 0:
        return -1
    if len(data) == 1:
        return data[0]

    low = 0
    high = len(data) - 1
    closest_value = float('inf')
    min_diff = float('inf')

    while low <= high:
        diff_low = abs(data[low] - key)
        diff_high = abs(data[high] - key)

        if min_diff < diff_low and min_diff < diff_high:
            low += 1
            high -= 1
        elif diff_low < diff_high:
            min_diff = diff_low
            closest_value = data[low]
            low += 1
        else:
            min_diff = diff_high
            closest_value = data[high]
            high -= 1
        print(diff_low, diff_high, closest_value)

    return closest_value


def main():
    data = [2, 3, 5, 8, 13, 21, 34, 55, 89, 144]
    key = 4
    if type(data[0]) != type(key):
        raise TypeError('data and key must be the same type')
    print(find_closest(data, key))

if __name__ == '__main__':
    main()
