count = 0
l = []


def get_yushu(num):
    global count, l
    gaowei = num // 10
    yushu = num % 10
    count += 1
    l.append(yushu)
    if gaowei == 0:
        return

    # get_yushu(gaowei)


if __name__ == '__main__':
    get_yushu(123)
    print(l)