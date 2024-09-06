# 输入获取
# arr = list(map(int, list(input())))
# arr = [2, 0]
#
# # 算法入口
# def getResult():
#     correct = 0
#     for i in range(len(arr)):
#         fault = arr[i]
#         if fault > 4:
#             fault -= 1
#
#         # for j in range(len(arr) - i - 1, 0, -1):
#         #     fault *= 9
#         fault = fault * 9 ** (len(arr) - i - 1)
#
#
#         correct += fault
#     return correct
#
#
# # 调用算法
# print(getResult())



def matrixZip(matrix):
    # cols = len(matrix[0])
    rows = len(matrix)
    # zip = [0 for i in range(cols)]
    #
    # for c in range(cols):
    #     for r in range(rows):
    #         zip[c] += matrix[r][c]
    #
    # return zip
    for i in range(rows):
        for j in range(i+1, rows+1):
            print(matrix[i: j])


matrix = [[1,2,3],[4,5,6],[7,8,9]]
matrixZip(matrix)