def sum_num(x):
    k = 0
    while x > 0:
        k += x % 10
        x //= 10
    return k


def main():
    n = int(input())
    a = list(map(int, input().split()))
    sum_num_a = sum_num

    a.sort()
    a.sort(key=lambda x: sum_num(x))

    print(*a)


if __name__ == '__main__':
    main()
