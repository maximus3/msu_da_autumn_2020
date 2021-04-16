def brackets(n, o=0, c=0, s=''):
    if c == n:
        yield s
    if o < n:
        yield from brackets(n, o + 1, c, s + '(')
    if c < o:
        yield from brackets(n, o, c + 1, s + ')')


if __name__ == '__main__':
    for i in brackets(int(input())):
        print(i)
