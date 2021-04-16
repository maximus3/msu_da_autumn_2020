def main():
    sn, k = input().split()
    n, k = int(sn), int(k)

    s = 0
    cur = ''

    for i in range(k):
        cur += sn
        s += int(cur)

    print(s)


if __name__ == '__main__':
    main()
