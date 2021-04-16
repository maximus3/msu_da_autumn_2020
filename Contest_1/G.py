def main():
    a = list(map(int, input().split()))

    min1 = a[0]
    min2 = a[1]
    max1 = a[0]
    max2 = a[1]

    if max1 < max2:
        max1, max2 = max2, max1
    if min1 > min2:
        min1, min2 = min2, min1

    for elem in a[2:]:
        if elem < min1:
            min2 = min1
            min1 = elem
        elif elem < min2:
            min2 = elem

        if elem > max1:
            max2 = max1
            max1 = elem
        elif elem > max2:
            max2 = elem

    if min1 * min2 > max1 * max2:
        print(min1, min2)
    else:
        print(max2, max1)


if __name__ == '__main__':
    main()
