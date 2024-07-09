def bub_sort(a):
    n = len(a)
    for i in range(n):
        for j in range(0, n-i-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                print(a)  
    return a  

a = list(map(int, input("Enter the elements: ").split()))

print("Sorted list:",bub_sort(a) )
