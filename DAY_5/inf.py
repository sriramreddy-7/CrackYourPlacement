# n=int(input())
# arr=[]
# for i in range(n):
#     x=
#     y
# e=int(input())
# def subsets(arr):
#     # res=[[]]
#     # for i in arr:
#     #     res+=[curr+[i] for curr in res]
#     # return res
#     for i in range(1,arr.length):
#         print(i)
# arr=[1,2,3]
# print(subsets(arr))
def longest_subarray_same_elements(arr):
    if not arr:
        return 0

    max_length = 1
    current_length = 1

    for i in range(1, arr.length):
        if arr[i] == arr[i - 1]:
            current_length += 1
        else:
            max_length = max(max_length, current_length)
            current_length = 1

    max_length = max(max_length, current_length)

    return max_length

# Example usage
arr = [1, 2, 2, 2, 3, 3, 1, 1, 1, 1]
print(longest_subarray_same_elements(arr))  # Output: 4
