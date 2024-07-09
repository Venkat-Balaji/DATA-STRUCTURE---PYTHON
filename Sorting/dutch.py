def dutch(a):
    n = len(a)
    low,mid,high=0,0,n-1
    while(mid<=high):
        if a[mid]==0:
            a[low],a[mid]=a[mid],a[low]
            low+=1
            mid+=1
        elif a[mid]==1:
            mid+=1
        elif a[mid]==2:
            a[high],a[mid]=a[mid],a[high]
            high-=1
        print(a)  
    return a  

a = list(map(int, input("Enter the elements: ").split()))

print("Sorted list:",dutch(a) )