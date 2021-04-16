import re
import operator
from itertools import starmap
from functools import reduce


def solution1(x):
    return list(map(lambda s: int(''.join(re.findall(r'\d+', s))[::-1]), x))


def solution2(x):
    return list(starmap(operator.mul, x))


def solution3(x):
    return list(filter(lambda x: x % 6 == 0 or x % 6 == 2 or x % 6 == 5, x))


def solution4(x):
    return list(filter(lambda x: x, x))


def solution5(rooms):
    list(map(operator.setitem, rooms, ['square'] * len(rooms),
             map(operator.mul, map(operator.getitem, rooms,
                 ['width'] * len(rooms)),
             map(operator.getitem, rooms, ['length'] * len(rooms)))
             ))
    return rooms


def solution6(rooms):
    n = len(rooms)
    return list(map(dict, list(zip(
        list(zip(['name'] * n, map(operator.getitem, rooms, ['name'] * n))),
        list(zip(['width'] * n, map(operator.getitem, rooms, ['width'] * n))),
        list(zip(['length'] * n,
             map(operator.getitem, rooms, ['length'] * n))),
        list(zip(['square'] * n,
                 map(operator.mul, map(operator.getitem, rooms, ['width'] * n),
                 map(operator.getitem, rooms, ['length'] * n))
                 )),
        ))))


def solution7(x):
    return reduce(lambda x, y: x.intersection(y), x)


def solution8(x):
    return reduce(lambda x, y: (operator.setitem(x, y,
                                operator.getitem(x, y) + 1) if x.get(y)
                                else operator.setitem(x, y, 1)) or x, x, {})


def solution9(students):
    students_new = list(filter(lambda x: x['gpa'] > 4.5, students))
    return list(map(operator.getitem, students_new,
                    ['name'] * len(students_new)))


def solution10(x):
    return list(filter(lambda x:
                       sum(map(int, x[::2])) == sum(map(int, x[1::2])), x))


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
    assert solution1(['12', '25.6', '84,02',
                      '  69-91']) == [21, 652, 2048, 1996]
    assert solution2(zip(range(2, 5), range(3, 9, 2))) == [6, 15, 28]
    assert solution3(range(20)) == [0, 2, 5, 6, 8, 11, 12, 14, 17, 18]
    assert solution4(['', 25, None, 'python', 0.0, [],
                      ('msu', '1755-01-25')]) == [25, 'python',
                                                  ('msu', '1755-01-25')]

    rooms = [
        {"name": "комната1", "width": 2, "length": 4},
        {"name": "комната2", "width": 2.5, "length": 5.6},
        {"name": "кухня", "width": 3.5, "length": 4},
        {"name": "туалет", "width": 1.5, "length": 1.5},
    ]

    assert solution5(rooms) == [
        {"name": "комната1", "width": 2, "length": 4, "square": 8},
        {"name": "комната2", "width": 2.5, "length": 5.6, "square": 14.0},
        {"name": "кухня", "width": 3.5, "length": 4, "square": 14.0},
        {"name": "туалет", "width": 1.5, "length": 1.5, "square": 2.25},
    ]
    assert rooms == [
        {"name": "комната1", "width": 2, "length": 4, "square": 8},
        {"name": "комната2", "width": 2.5, "length": 5.6, "square": 14.0},
        {"name": "кухня", "width": 3.5, "length": 4, "square": 14.0},
        {"name": "туалет", "width": 1.5, "length": 1.5, "square": 2.25},
    ]

    rooms = [
        {"name": "комната1", "width": 2, "length": 4},
        {"name": "комната2", "width": 2.5, "length": 5.6},
        {"name": "кухня", "width": 3.5, "length": 4},
        {"name": "туалет", "width": 1.5, "length": 1.5},
    ]
    assert solution6(rooms) == [
        {"name": "комната1", "width": 2, "length": 4, "square": 8},
        {"name": "комната2", "width": 2.5, "length": 5.6, "square": 14.0},
        {"name": "кухня", "width": 3.5, "length": 4, "square": 14.0},
        {"name": "туалет", "width": 1.5, "length": 1.5, "square": 2.25},
    ]
    assert rooms == [
        {"name": "комната1", "width": 2, "length": 4},
        {"name": "комната2", "width": 2.5, "length": 5.6},
        {"name": "кухня", "width": 3.5, "length": 4},
        {"name": "туалет", "width": 1.5, "length": 1.5},
    ]

    assert solution7([{1, 2, 3, 4, 5}, {2, 3, 4, 5, 6},
                      {3, 4, 5, 6, 7}]) == {3, 4, 5}
    assert solution8([1, 2, 1, 1, 3, 2, 3, 2, 4, 2, 4]) == {1: 3, 2: 4,
                                                            3: 2, 4: 2}

    students = [
        {'name': 'Alina', 'gpa': 4.57},
        {'name': 'Sergey', 'gpa': 5.0},
        {'name': 'Nastya', 'gpa': 4.21},
        {'name': 'Valya', 'gpa': 4.72},
        {'name': 'Anton', 'gpa': 4.32},
    ]
    assert solution9(students) == ['Alina', 'Sergey', 'Valya']
    assert solution10(['165033', '477329', '631811', '478117', '475145',
                       '238018', '917764', '394286']) == ['165033', '475145',
                                                          '238018']
    print("Tests OK")
