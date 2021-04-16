def main():
    a = list(map(int, input().split()))

    q_start = a[0]
    q_prev = a[0]
    dist = 0
    for q in a[1:]:
        if dist == 0 and q == q_start:
            print(q_start, q_start + 1, 1)
            continue
        if dist == 0:
            q_prev = q
            dist = q - q_start
            continue
        if q - q_prev == dist:
            q_prev = q
        else:
            print(q_start, q_prev + 1 if dist > 0 else q_prev - 1, dist)
            q_start = q
            q_prev = q
            dist = 0
    if dist == 0:
        dist = 1
    print(q_start, q_prev + 1 if dist > 0 else q_prev - 1, dist)


if __name__ == '__main__':
    main()
