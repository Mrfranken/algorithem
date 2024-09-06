def count_subarrays(N, x, arr):
    count = 0
    window_sum = 0
    left = 0
    for right in range(N):
        # 将右边的元素加入当前窗口
        window_sum += arr[right]
        # 当当前窗口的和大于等于x时，移动左边界，直到窗口的和小于x
        while window_sum >= x:
            count += N - right  # 以right结尾的子数组个数
            window_sum -= arr[left]  # 移除窗口最左边的元素
            left += 1
    return count


# 读取输入
# N, x = map(int, input().split())
# arr = list(map(int, input().split()))
# 计算结果并打印输出
arr = [2, 3, 4, 5, 6, 7]
N = 6
x = 8
result = count_subarrays(N, x, arr)
print(result)
