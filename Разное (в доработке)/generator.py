from random import choice, randint

RESOURCE = 'abcdef'
SAMPLE_LEN = 100
ITERATIONS = 5

def find_gen(array, goal):
    print(f'в "{array}" находим "{goal}" по следующим индексам - ', end=" ")
    for index in range(len(array)):
       if array[index] !=goal:
            continue
       print(index, end=" ")
       yield index

def find(array, goal):
    index_list = [i for i in range(len(array)) if goal == array[i]]
    print(f'в "{array}" находим "{goal}" по следующим индексам - {index_list}')
    return index_list

def test_find(resource=RESOURCE, sample_len=SAMPLE_LEN):
    sample = "".join([choice(resource) for _ in range(sample_len)])
    goal = resource[randint(0, len(resource)-1)]
    find(sample, goal)

if __name__ == '__main__':
    [test_find() for _ in range(ITERATIONS)]
    print()

    assert find('abcabab', 'a') == [0, 3, 5]
    print()

    for _ in find_gen('abcabab', 'a'):
        pass
