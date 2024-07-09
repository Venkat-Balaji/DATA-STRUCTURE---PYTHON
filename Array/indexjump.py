a=[1,0,1,1,5]
# a=[3,2,1,0,4]
n=len(a)
j=0
for i in range (0,n-1):
    if a[i]!=0:
        i=i+a[i]
        j=i
#         print(j)
#     else:
#         print("False")
#     if j==n-1:
#         break
# if j==n-1:
#     print("True")
# else:
#     print("False")

        if a[i]==0:
            break
if a[i]==0:
    print("False")
else:
    print("True")

        