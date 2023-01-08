def find_next_square(sq):
    # Return the next square if sq is a square, -1 otherwise

    return pow(sq ** .5 + 1, 2) if sq ** .5 == int(sq ** .5) else -1


if __name__ == '__main__':
    print(find_next_square(121))

