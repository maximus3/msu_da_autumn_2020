def solution1(x):
    return [c * 4 for c in x]


def solution2(x):
    return [elem * (i + 1) for i, elem in enumerate(x)]


def solution3(x):
    return [elem for elem in x if elem % 3 == 0 or elem % 5 == 0]


def solution4(x):
    return [elem[i] for elem in x for i in range(len([len(elem_in_x)
            for elem_in_x in x])) if i < len(elem)]


def solution5(n):
    return [(a, b, c) for a in range(3, 31) for b in range(3, 31)
            for c in range(3, 31)
            if a * a + b * b == c * c and c <= n and b < c and a < b]


def solution6(x):
    return [[elem + delta for elem in x[1]] for delta in x[0]]


def solution7(x):
    return [[elem[i] for elem in x] for i in range(len(x[0]))]


def solution8(x):
    return [[int(a) for a in elem.split()] for elem in x]


def solution9(x):
    return {chr(97 + i): i * i for i in x}


def solution10(x):
    return {s.lower().title() for s in x if len(s) > 3}


solutions = {
    'solution1': solution1,
    'solution2': solution2,
    'solution3': solution3,
    'solution4': solution4,
    'solution5': solution5,
    'solution6': solution6,
    'solution7': solution7,
    'solution8': solution8,
    'solution9': solution9,
    'solution10': solution10,
}

if __name__ == '__main__':
    assert solution1('python') == ['pppp', 'yyyy', 'tttt', 'hhhh',
                                   'oooo', 'nnnn']
    assert solution2('python') == ['p', 'yy', 'ttt', 'hhhh', 'ooooo', 'nnnnnn']
    assert solution3(range(16)) == [0, 3, 5, 6, 9, 10, 12, 15]
    assert solution4([[1, 2, 3], [4, 5, 6, 7], [8, 9], [0]]) == [1, 2, 3, 4, 5,
                                                                 6, 7, 8, 9, 0]
    assert solution5(15) == [(3, 4, 5), (5, 12, 13), (6, 8, 10), (9, 12, 15)]
    assert solution6(([0, 1, 2], [0, 1, 2, 3, 4])) == [[0, 1, 2, 3, 4],
                                                       [1, 2, 3, 4, 5],
                                                       [2, 3, 4, 5, 6]]
    assert solution7([[1, 2], [3, 4], [5, 6]]) == [[1, 3, 5], [2, 4, 6]]
    assert solution7([[1, 3, 5], [2, 4, 6]]) == [[1, 2], [3, 4], [5, 6]]
    assert solution8(["0", "1 2 3", "4 5 6 7", "8 9"]) == [[0], [1, 2, 3],
                                                           [4, 5, 6, 7],
                                                           [8, 9]]
    assert solution9(range(0, 7)) == {'a': 0, 'b': 1, 'c': 4, 'd': 9, 'e': 16,
                                      'f': 25, 'g': 36}
    assert solution10(['Alice', 'vova', 'ANTON', 'Bob', 'kAMILA', 'CJ',
                       'ALICE', 'Nastya']) == {'Alice', 'Anton', 'Kamila',
                                               'Nastya', 'Vova'}
    print("Tests OK")
