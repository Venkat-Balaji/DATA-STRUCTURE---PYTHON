a=[3,4,5,6,7,8,9]
k=1
n=len(a)
r=[]
# for i in range(0,n):
#     if i<k:
#         m=a[n+i-k]
#         r.append(m)
        
#     else:
#         m=a[i-k]
#         r.append(m)
        
# print(r)
for i in range(k):
    b=a.pop(-1)
    a.insert(b)
print(a)