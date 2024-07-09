# a=[3,2,5,4]
a=list(map(int,input("Enter The Elements:").split()))
a.sort()

n=len(a)
t=n//2
m=0


for i in range (n):
    while a[i] != a[t]:
        if a[t]<a[i]:
            a[i]-=1
        elif a[t]>a[i]:
            a[i]+=1
        m+=1
print("Element=",a[t],"Moves=",m)

