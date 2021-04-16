def main():
    n = int(input())
    a = list(map(int, input().split()))
    a_set = set(a)
    k = len(a) - len(a_set)
    ans = []
    for q in a:
        if q in a_set:
            a_set.remove(q)
            ans.append(q)
    print(*ans)
    print(k)


if __name__ == '__main__':
    main()
