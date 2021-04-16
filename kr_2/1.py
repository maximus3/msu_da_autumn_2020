def main():
    x = list(map(int, input().split()))
    s = sum(x)
    n = int(input())
    if s < n:
        return
    l_x = len(x)
    best_i = 0
    best_j = l_x
    best_len = l_x

    i, j = 0, 0
    cur_sum = 0
    while j != l_x:
        cur_sum += x[j]
        j += 1
        while cur_sum >= n:
            if j - i < best_len:
                best_len = j - i
                best_i, best_j = i, j
                if best_len == 1:
                    break
            cur_sum -= x[i]
            i += 1

    print(*x[best_i:best_j])


if __name__ == '__main__':
    main()
