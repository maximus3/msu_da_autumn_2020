def main():
    s1 = input().lower().split()
    s2 = input().lower().split()
    s1.sort()
    s2.sort()

    i = 0
    j = 0

    l1 = len(s1)
    l2 = len(s2)

    while True:
        if i == l1:
            if j < l2:
                print('NO')
                return
            break
        if j == l2:
            break
        if s1[i] == s2[j]:
            i += 1
            j += 1
        else:
            i += 1

    print('YES')


if __name__ == '__main__':
    main()
