# 输入获取
n = int(input())
arr = list(map(int, input().split(" ")))


# 算法入口
def getResult():
    arr.sort()

    if arr[0] == 1:
        return 1

    color = [False]*n
    count = 0

    for i in range(n):
        if color[i]:
            continue

        color[i] = True
        for j in range(i+1, n):
            if not color[j] and arr[j] % arr[i] == 0:
                color[j] = True

        count += 1

    return count


# 调用算法
print(getResult())