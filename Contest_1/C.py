def main():
    x = float(input())

    x = round(x * 100)

    nom = [1000, 500, 200, 100, 50, 10, 5, 1]
    ans = {}

    for num in nom:
        while x >= num:
            if num not in ans:
                ans[num] = 0
            ans[num] += 1
            x -= num

    for num in ans:
        print('{0:5.2f}\t{1}'.format(num / 100, ans[num]))


if __name__ == '__main__':
    main()
