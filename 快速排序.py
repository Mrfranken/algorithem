def quick_sort(arr, start, end):
    """
    https://blog.csdn.net/qq_35164554/article/details/114123001
    """
    # 递归的出口
    if start >= end:
        return
    # 需要三个变量，分别记录要找位置的数值（默认为第一个，存在to_sort中），左边的low游标，右边的high游标
    to_sort = arr[start]
    # 左边游标
    low = start
    # 右边游标
    high = end
    # 当low >= high的时候，说明完成了一个元素位置的查找，跳出循环
    while low < high:
        # 控制右边游标的移动，如果数字比to_sort大或者相等，游标持续左移，不满足条件时，将值赋给另一个游标
        while low < high and arr[high] >= to_sort:
            high -= 1
        arr[low], arr[high] = arr[high], arr[low]
        # 控制左边游标的移动，如果数字比to_sort小，游标持续右移，不满足条件时，将值赋给另一个游标
        while low < high and arr[low] < to_sort:
            low += 1
        arr[high], arr[low] = arr[low], arr[high]
    # 剩下一个low的坑，用来放to_sort
    # arr[low] = to_sort
    # 这个地方用递归，对左右两边的排列再次调用快排
    quick_sort(arr, start, low - 1)
    quick_sort(arr, low + 1, end)


arr1 = [20, 87, 45, 89, 8, 32, 10]
# arr1 = [10, 8, 20, 89, 45, 32, 87]
quick_sort(arr1, 0, len(arr1) - 1)
print(arr1)
