from librarys_modules.pytest_.file_workers import read_from_file
import pytest

def test_read_from_file():
    with open('tests/testfile.txt', 'w'):
        pass
    test_data = ['one\n', 'two\n', 'three\n']
    with open('tests/testfile.txt', 'a') as f_o:
        f_o.writelines(test_data)
    assert test_data == read_from_file('tests/testfile.txt')


# def test_read_from_file2():
#     test_data = ['one\n', 'two\n', 'three\n']
#     assert test_data == read_from_file('tests/testfile.txt')
