def str_len(data):
    if data == '':
        return 0
    return 1 + str_len(data[1:])

def main():
    data = "aeiou"
    print(str_len(data))

if __name__ == '__main__':
    main()
