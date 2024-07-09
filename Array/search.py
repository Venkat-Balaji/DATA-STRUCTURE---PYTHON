l=list(map(int,input("Enter the elements:").split()))
# l=[5,7,8,5,5]
n=len(l)
t=int(input("Enter the Target element:"))
for i in range(0,n):
    if l[i]==t:
        print("index value = ",i)
