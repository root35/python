def binary_search_rec(data, key):
    if data is None:
        return
    mid_index = len(data) // 2
    if key == data[mid_index]:
        return 1
    elif key < data[mid_index]:
        return binary_search_rec(data[0:mid_index], key)
    else:
        return binary_search_rec(data[mid_index:len(data)], key)

def main():
    data = [2, 3, 5, 8, 13, 21, 34, 55, 89, 144]
    key = 89
    if type(data[0]) != type(key):
        raise TypeError('data and key must be the same type')
    print(binary_search_rec(data, key))


if __name__ == '__main__':
    main()
