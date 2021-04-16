def main():
    n = int(input())
    d = {}
    for i in range(n):
        s = input()
        let_s = tuple(sorted(list(s)))
        if let_s in d:
            d[let_s].append(s)
        else:
            d[let_s] = [s]

    for let_s in d:
        print(*d[let_s])


if __name__ == '__main__':
    main()
