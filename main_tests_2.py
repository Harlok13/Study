def bouncing_ball(h, bounce, window):
    if not h > 0 or 0 > bounce >= 1 or not window < h:
        return -1
    assert h > 0
    assert window < h
    assert 0 < bounce < 1
    res = 1
    while h > window:
        h *= bounce
        if h > window:
            res += 2
        else:
            break
    return res


if __name__ == '__main__':
    print(bouncing_ball(3000000000000000000000000000000000000000000000000000000000000000000000000000, 0.99, 0.000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001))
