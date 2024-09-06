# def hex_to_int(hex):
#     return int(hex, 16)
#
#
# tag = input("Enter the tag: ")  # 输入信元的 Tag
# byte_stream = input("Enter the byte stream: ")  # 输入字节流
# byte_tokens = byte_stream.strip().split(" ")  # 将字节流拆分成字符串数组
# byte_count = len(byte_tokens)  # 字节的个数
# value = []  # 存储解码后的 value
# length = 0  # 信元 value 的长度
# i = 0
# while i < byte_count:
#     length = hex_to_int(byte_tokens[i + 2]) * 256 + hex_to_int(byte_tokens[i + 1])  # 根据小端序合并字节得到 Length 的值
#     if hex_to_int(byte_tokens[i]) == hex_to_int(tag):  # 如果当前字节的 Tag 和输入的 Tag 相同
#         for j in range(length):
#             value.append(byte_tokens[i + 3 + j])  # 提取后续的 Length 个字节作为 Value
#         break
#     i += (length + 3)
# result = " ".join(value)  # 将 value 转换为字符串，并使用空格分隔元素
# print(result)  # 输出解码后的值

def generate_permutations(current, nums, result):
    if len(current) == len(nums):
        result.append(current)
    else:
        for num in nums:
            if num not in current:
                generate_permutations(current + [num], nums, result)


current = []
nums = [1, 2, 3]
result = []

generate_permutations(current, nums, result)
print(result)
