def witty_delivery_man():
    # N, M = map(int, input().split())  # 输入当前楼层N和目标楼层M
    N = 5
    M = 17
    if N >= M:
        return 0
    dp = [0] * (M + 1)  # 创建dp列表，dp[i]表示到达第i层的最短时间
    for i in range(N + 1):
        dp[i] = N - i  # 初始化到N层以下需要的时间，步行一层需要1分钟
    # for i in range(N + 1, M + 1):
    tmp = N
    while tmp <= M:
        i = tmp
        if i % 2 == 0:
            dp[i] = min(dp[i - 1] + 1, dp[i // 2] + 1)  # 偶数层可以通过步行梯或电梯到达，选择最短时间
        else:
            dp[i] = min(dp[i - 1] + 1, dp[(i + 1) // 2] + 2)  # 奇数层需要先上一层或下一层，再乘坐电梯，选择最短时间
        tmp += 1
    return dp[M]  # 返回到达目标楼层M的最短时间


# 调用函数计算最短送达时间
result = witty_delivery_man()
# 输出结果
print(result)
