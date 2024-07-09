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


m=C-1
for i in range(R):
     for j in range(m,-1,-1):
        print(matrix[j][i], end = " ")
        
     print()