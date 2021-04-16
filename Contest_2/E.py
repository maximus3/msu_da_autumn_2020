from itertools import islice


def chain_loop(args):
    have_elements = [True] * len(args)
    count = len(args)

    args = list(map(lambda elem: iter(elem), args))
    while count:
        for j, elem in enumerate(args):
            if have_elements[j]:
                try:
                    yield next(elem)
                except StopIteration:
                    have_elements[j] = False
                    count -= 1


if __name__ == "__main__":
    a = range(5)
    b = range(10)
    c = range(3)

    assert list(chain_loop([a, b, c])) == [0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 4,
                                           4, 5, 6, 7, 8, 9]

    a = [None, None, None]
    b = [1] * 5

    assert list(chain_loop([a, b])) == [None, 1, None, 1, None, 1, 1, 1]

    a = (i for i in range(10))
    b = a

    assert list(chain_loop([a, b])) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    from itertools import tee

    a = (i for i in range(3))

    assert list(chain_loop(tee(a, 5))) == [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2,
                                           2, 2, 2]

    print("Tests OK")
