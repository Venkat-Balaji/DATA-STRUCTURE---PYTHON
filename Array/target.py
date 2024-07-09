
s=int(input("Enter the number of elements:"))
l=list(map(int,input("Enter the elements: ").split()))

t=int(input("Enter the Target element:"))
for i in range(0,s):
    for j in range(i+1,s):
        if (l[i]+l[j]) ==t:
            print(l[i],l[j])
        

