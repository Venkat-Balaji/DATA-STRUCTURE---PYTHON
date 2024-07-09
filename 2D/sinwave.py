R = int(input("Enter the number of rows:"))
C = int(input("Enter the number of columns:"))
 
b=1

matrix = []

for i in range(R):          
    a =[]
    for j in range(C):      
         a.append(int(input(f"Enter the element {b}({i},{j}):")))
         b+=1    
    matrix.append(a)
m=R-1
for i in range(R):
    for j in range(C):
        print(matrix[i][j], end = " ")
    print()

u=[]
for j in range(C):
    
         
     if j%2==0:
        for i in range(R):
           u.append(matrix[i][j])
     else:
         for i in range(m,-1,-1):
             u.append(matrix[i][j])
print(u)
               