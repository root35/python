def find_uppercase(data, start=0, upper=[]):
    if start < len(data):
        if data[start].isupper():
            upper.append(data[start])
        return find_uppercase(data, start+1, upper)
    return upper

def main():
    print(find_uppercase('FindUpperC'))

if __name__ == '__main__':
    main()
