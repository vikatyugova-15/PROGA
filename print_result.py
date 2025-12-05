def print_result(test):
    def wrapper():
        print(test.__name__)
        if type(test())==list:
            print(*test(), sep='\n')
        elif type(test())==dict:
            print(*[f"{k} = {v}" for k, v in test().items()], sep='\n')
        else:
            print(test())
    return wrapper

@print_result
def test_1():
    return 1


@print_result
def test_2():
    return 'iu5'


@print_result
def test_3():
    return {'a': 1, 'b': 2}


@print_result
def test_4():
    return [1, 2]


if __name__ == '__main__':
    print('!!!!!!!!')
    test_1()
    test_2()
    test_3()
    test_4()