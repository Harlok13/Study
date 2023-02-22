import pytest

collections_not_dict = [list, tuple]


def flatten_dict(nested_lists):
    res = []
    for key, value in nested_lists.items():
        res.append(key)

        if not isinstance(value, dict):
            if type(value) in collections_not_dict:
                res += linear(value)
            else:
                res.append(value)
        else:
            res += flatten_dict(value)
    return res


def linear(nested_lists):
    res = []
    for elem in nested_lists:
        if isinstance(elem, int) or isinstance(elem, str):
            res.append(elem)
        elif isinstance(elem, dict):
            res += flatten_dict(elem)
        else:
            res += linear(elem)
    return res


TEST_DATA = ([1, 'abc', [[100, 200], 10, 20], [30, 40]],
             [[1, '2', 3], (4, 5), [6, {'7': {8: [9, 10]}}], 11, 12, [13, 14, 15], [16], 17,
              [[18], [19, 20, [[[21]]]], {22: (23, '24')}]]
             )
EXPECTED = ([1, 'abc', 100, 200, 10, 20, 30, 40],
            [1, '2', 3, 4, 5, 6, '7', 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, '24'])


@pytest.mark.parametrize('nested_lists, expected',
                         (pytest.param([1, 'abc', [[100, 200], 10, 20], [30, 40]], [1, 'abc', 100, 200, 10, 20, 30, 40],
                                       id="[1, 'abc', 100, 200, 10, 20, 30, 40]"),
                          pytest.param([[1, '2', 3], (4, 5), [6, {'7': {8: [9, 10]}}], 11, 12, [13, 14, 15], [16], 17,
                                        [[18], [19, 20, [[[21]]]], {22: (23, '24')}]],
                                       [1, '2', 3, 4, 5, 6, '7', 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21,
                                        22, 23,
                                        '24'],
                                       id="[1, '2', 3, 4, 5, 6, '7', 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, '24']")

                          ))
def test_linear(nested_lists, expected):
    assert linear(nested_lists) == expected
    assert True


if __name__ == '__main__':
    for indx in range(2):
        assert linear(TEST_DATA[indx]) == EXPECTED[indx], f'{linear(TEST_DATA[indx])}'
