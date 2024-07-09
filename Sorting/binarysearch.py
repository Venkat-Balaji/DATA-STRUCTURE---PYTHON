a = list(map(int, input("Enter the elements:").split()))
n = len(a)
a.sort()
num = int(input("Target:"))
print("sorted list: ",a)
l = 0
r = n - 1
found = False

while l <= r:
    mid = (l + r) // 2
    if a[mid] < num:
        l = mid + 1
    elif a[mid] > num:
        r = mid - 1
    else:
        print("index:",mid)
        found = True
        break

if not found:
    print("Number not found")
