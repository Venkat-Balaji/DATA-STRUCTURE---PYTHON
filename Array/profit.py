n=int(input("Enter the number of elements:"))
l=list(map(int,input().split()))
# t=int(input("day"))
maxi=[]
for i in range (0,n-1):
    if l[i]!=max(l):
        for j in range(i+1,n-1):
            if l[j]>l[i]:
                a=l[j]-l[i]
                maxi.append(a)
            
print(max(maxi))
print(maxi)



