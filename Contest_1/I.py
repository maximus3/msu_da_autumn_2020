import sys


def safe_input():
    try:
        return input()
    except EOFError:
        sys.exit(0)


def main(q_count=7, max_dist=1):
    x_start = 1
    x_finish = 100000

    s = 0

    while x_start != x_finish:
        d = (x_finish - x_start + 1) // (q_count + 1)
        while d < max_dist and q_count > 1:
            q_count -= 1
            d = (x_finish - x_start + 1) // (q_count + 1)

        q_nums = [i for i in range(x_start + d, x_finish + 1, d)]
        q_nums = q_nums[:q_count]

        for num in q_nums:
            print(f'? {num}', flush=True)
        print('+', flush=True)

        ans = []

        for i in range(q_count):
            ans.append(int(safe_input()))

        for i, num in enumerate(q_nums):
            if ans[i]:
                x_finish = min(x_finish, num - 1)
            else:
                x_start = max(x_start, num)

        s += 10 + q_count

        # print(f'>> {x_start} {x_finish}, SUM={s}', flush=True)

    print(f'! {x_start}', flush=True)


if __name__ == '__main__':
    main(7, 1)
