def nb_year(p0, percent, aug, p):
    counter = 0
    x = p0
    while x < p:
        x = x + x * (percent / 100)
        x += aug
        counter += 1
    return counter


if __name__ == '__main__':
    print(nb_year(1500, 5, 100, 5000))
