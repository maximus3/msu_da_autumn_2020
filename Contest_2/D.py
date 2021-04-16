import functools


def counter(func):
    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        if not hasattr(wrapped, 'no_need_reset'):
            wrapped.no_need_reset = 0
            wrapped.rdepth = 0
            wrapped.ncalls = 0
            func.rdepth = 0
            func.ncalls = 0

        if not wrapped.no_need_reset:
            wrapped.rdepth = 0
            wrapped.ncalls = 0

        wrapped.no_need_reset += 1

        func.ncalls += 1
        func.rdepth += 1

        result = func(*args, **kwargs)

        wrapped.rdepth = max(wrapped.rdepth, func.rdepth)
        wrapped.ncalls += func.ncalls

        func.rdepth -= 1
        func.ncalls = 0

        wrapped.no_need_reset -= 1

        return result
    return wrapped


def test_func(func, ncalls, rdepth, *args, **kwargs):
    func(*args, **kwargs)
    assert (func.ncalls, func.rdepth) == (ncalls, rdepth), (func.ncalls,
                                                            func.rdepth)


def tests():
    @counter
    def func_1():
        return

    @counter
    def func_2(n, steps):
        if steps == 0:
            return

        func_2(n + 1, steps - 1)
        func_2(n - 1, steps - 1)

    @counter
    def func_3(n):
        if n < 3:
            return 1
        else:
            return func_3(n - 2) + func_3(n - 1)

    @counter
    def func_4(n):
        if n < 2:
            return 1
        else:
            return func_4(n - 1)

    @counter
    def func_5(n):
        if n < 2:
            return func_1()
        else:
            return func_5(n - 1)

    test_func(func_1, 1, 1)
    test_func(func_1, 1, 1)

    test_func(func_2, 63, 6, 0, 5)
    test_func(func_2, 15, 4, 0, 3)

    test_func(func_3, 3, 2, 3)
    test_func(func_3, 5, 3, 4)
    test_func(func_3, 9, 4, 5)
    test_func(func_3, 15, 5, 6)
    test_func(func_3, 25, 6, 7)
    test_func(func_3, 41, 7, 8)
    test_func(func_3, 67, 8, 9)
    test_func(func_3, 109, 9, 10)

    test_func(func_4, 1, 1, 1)
    test_func(func_4, 2, 2, 2)
    test_func(func_4, 3, 3, 3)
    test_func(func_4, 4, 4, 4)
    test_func(func_4, 134, 134, 134)

    test_func(func_5, 1, 1, 1)
    test_func(func_5, 2, 2, 2)
    test_func(func_5, 3, 3, 3)
    test_func(func_5, 4, 4, 4)
    test_func(func_5, 134, 134, 134)


if __name__ == "__main__":
    tests()
    print("Tests OK")
