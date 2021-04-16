from collections import defaultdict
import itertools


def smartdict_nan(key):
    return itertools.repeat(10 * key).__next__


N = 10

smartdict = {}
for key in range(N):
    val = defaultdict(smartdict_nan(key))
    smartdict[key] = val

# Код работает не верно, так как каждый раз при вызове
# lambda-функции функция обращается к переменной key.
# То есть при обращении к несуществующему элементу словаря
# вызывается функция, которая обращается к переменной key.
# Если удалить переменную key (del key), то это приведет
# к ошибке при попытке вызове лямбда-функции:
# NameError: name 'key' is not defined
# Чтобы исправить это, можно использовать функцию repeat
# Из модуля itertools.
