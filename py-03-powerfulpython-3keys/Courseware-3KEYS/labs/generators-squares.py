def gen_squares(max_root):
    for root in range(max_root):
        yield root**2


squares = gen_squares(5)
for square in squares:
    print(square)
