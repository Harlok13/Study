def foo(num: str) -> bool:
    return bool([i for i in set(num) if num.count(i) == 3])


if __name__ == '__main__':
    assert foo('4544') == True
    assert foo('4844') == True
    assert foo('4814') == False
    assert foo('1978') == False
    assert foo('2922') == True
