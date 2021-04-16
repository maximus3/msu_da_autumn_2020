def merge_sort(x):
    x = list(x)
    count = 1
    l_x = len(x)
    if l_x < 2:
        yield x
        return
    while count < l_x:
        count <<= 1
        new_x = []
        for i in range(0, l_x, count):
            len_mas = count >> 1
            x_left = x[i:i + len_mas]
            x_right = x[i + len_mas:i + count]
            l_idx, r_idx = 0, 0
            while l_idx != len(x_left) or r_idx != len(x_right):
                if l_idx == len(x_left):
                    new_x.append(x_right[r_idx])
                    r_idx += 1
                elif r_idx == len(x_right):
                    new_x.append(x_left[l_idx])
                    l_idx += 1
                else:
                    if x_left[l_idx] < x_right[r_idx]:
                        new_x.append(x_left[l_idx])
                        l_idx += 1
                    else:
                        new_x.append(x_right[r_idx])
                        r_idx += 1
        x = new_x
        yield new_x


if __name__ == '__main__':
    x = list(merge_sort([5, 3, 4, 6]))
    assert x == [[3, 5, 4, 6], [3, 4, 5, 6]], x

    x = list(merge_sort([1, 0]))
    assert x == [[0, 1]], x

    x = list(merge_sort([1, 0, -1]))
    assert x == [[0, 1, -1], [-1, 0, 1]], x

    x = list(merge_sort([1, 0, -1, -100, -3]))
    assert x == [[0, 1, -100, -1, -3], [-100, -1, 0, 1, -3], [-100, -3, -1, 0, 1]], x

    x = list(merge_sort([1]))
    assert x == [[1]], x

    x = list(merge_sort([3, 4, 4, 2, 9, 8, 7]))
    assert x == [[3, 4, 2, 4, 8, 9, 7], [2, 3, 4, 4, 7, 8, 9], [2, 3, 4, 4, 7, 8, 9]], x
