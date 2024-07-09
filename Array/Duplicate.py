# n=int(input("Enter the number of elements:"))
l=list(map(int,input("Enter the elements:").split()))
# l=[5,7,8,5,5]
n=len(l)
maj=-1
for i in range(n):
    count=0
    for j in range(i+1,n):
        if l[i]==l[j]:
            count+=1
        # if (count>=2):
        #     print("Duplicate element=",l[i])
            
        if count >=2:
            maj = l[i]
            break
    if maj != -1:
        break

if maj != -1:
    print("Duplicate Element=", maj)
else:
    print("No Duplicate elements found!")