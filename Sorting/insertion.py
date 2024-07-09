def insert(a):
    n = len(a)
    for i in range(1,n):
        insert=i
        current=a.pop(i)
        for j in range(i-1,-1,-1):
            if a[j] >current:
                insert=j
        a.insert(insert,current)
        print(a)
    return a
a = list(map(int, input("Enter the elements: ").split()))

print("Sorted list:",insert(a) )

# import sys
# input = sys.stdin.read

# data = input().split()

# index = 0
# T = int(data[index])
# index += 1

# results = []

# for _ in range(T):
#     N = int(data[index])
#     index += 1
#     arr = list(map(int, data[index:index + N]))
#     index += N
#     K = int(data[index])
#     index += 1
    
#     # Finding pivot
#     low, high = 0, N - 1
#     pivot = -1
#     while low <= high:
#         mid = (low + high) // 2
#         if mid < high and arr[mid] > arr[mid + 1]:
#             pivot = mid
#             break
#         if mid > low and arr[mid] < arr[mid - 1]:
#             pivot = mid - 1
#             break
#         if arr[low] >= arr[mid]:
#             high = mid - 1
#         else:
#             low = mid + 1
    
#     # Binary search in the appropriate segment
#     def binary_search(arr, low, high, key):
#         while low <= high:
#             mid = (low + high) // 2
#             if arr[mid] == key:
#                 return mid
#             elif arr[mid] < key:
#                 low = mid + 1
#             else:
#                 high = mid - 1
#         return -1
    
#     if pivot == -1:
#         result = binary_search(arr, 0, N - 1, K)
#     elif arr[pivot] == K:
#         result = pivot
#     elif arr[0] <= K:
#         result = binary_search(arr, 0, pivot - 1, K)
#     else:
#         result = binary_search(arr, pivot + 1, N - 1, K)
    
#     results.append(result)

# for res in results:
#     print(res)