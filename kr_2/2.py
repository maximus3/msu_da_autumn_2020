import functools


def retry(check, n_attempts=5):
    def decorator(func):
        @functools.wraps(func)
        def wrapped(*args, **kwargs):
            count = n_attempts
            result = func(*args, **kwargs)
            if count is None or count < 1:
                count = None
            else:
                count -= 1
            while not check(result):
                if count is not None and count < 1:
                    raise RuntimeError("Expired number of retries")
                if count is not None:
                    count -= 1
                result = func(*args, **kwargs)
            return result
        return wrapped
    return decorator


def test_1():
    @retry(check=bool)
    def func(a):
        return a

    try:
        return func(3)
    except RuntimeError as e:
        return e


def test_2():
    gen = iter(range(100))

    @retry(check=lambda x: x >= 5, n_attempts=6)
    def func():
        return next(gen, -1)

    try:
        return func()
    except RuntimeError as e:
        return e


def test_3():
    gen = iter(range(2))

    @retry(check=lambda x: x >= 5, n_attempts=6)
    def func():
        return next(gen, -1)

    try:
        return func()
    except RuntimeError as e:
        return e


def test_4():
    gen = iter(range(1000))

    @retry(check=lambda x: x < 0, n_attempts=-1)
    def func():
        return next(gen, -1)

    try:
        return func()
    except RuntimeError as e:
        return e


def test_5():
    gen = iter(range(1000))

    @retry(check=lambda x: x < 0, n_attempts=0)
    def func():
        return next(gen, -1)

    try:
        return func()
    except RuntimeError as e:
        return e


if __name__ == '__main__':
    s = str(test_1())
    assert s == '3', s

    s = str(test_2())
    assert s == '5', s

    s = str(test_3())
    assert s == 'Expired number of retries', s

    s = str(test_4())
    assert s == '-1', s

    s = str(test_5())
    assert s == '-1', s
