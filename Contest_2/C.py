import functools
import signal


class TimeoutException(RuntimeError):
    def __init__(self, message=None):
        super().__init__(message)


def handler_alarm(signum, frame):
    raise TimeoutException("Timed out")


def timeout(seconds):
    def decorator(func):
        if seconds is None or seconds <= 0:
            return func

        @functools.wraps(func)
        def wrapped(*args, **kwargs):
            signal.signal(signal.SIGALRM, handler_alarm)
            signal.setitimer(signal.ITIMER_REAL, seconds)
            result = func(*args, **kwargs)
            signal.setitimer(signal.ITIMER_REAL, 0)
            signal.signal(signal.SIGALRM, signal.SIG_DFL)
            return result
        return wrapped
    return decorator


def test_1():
    from time import sleep

    @timeout(seconds=0.5)
    def func(x):
        sleep(0.1)

    try:
        func(1)
    except TimeoutException as e:
        return e

    @timeout(seconds=None)
    def func(x):
        sleep(1)

    try:
        func(1)
    except TimeoutException as e:
        return e

    @timeout(seconds=-1)
    def func(x):
        sleep(1)

    try:
        func(1)
    except TimeoutException as e:
        return e


def test_2():
    from time import sleep

    @timeout(seconds=0.5)
    def func():
        sleep(0.6)

    try:
        func()
    except TimeoutException as e:
        return str(e)


def test_3():
    from time import sleep

    @timeout(seconds=1)
    def func():
        sleep(0.1)

    try:
        func()
    except TimeoutException as e:
        return str(e)

    sleep(10)


if __name__ == '__main__':
    assert test_1() is None
    assert test_2() == 'Timed out'
    assert test_3() is None
    print("Tests OK")
