n=int(input("Enter number of rows "))
m=int(input("Enter number of columns "))
mat=[]
print("Enter elements :")
for i in range(0,n):
    arr=[]
    for j in range(0,m):
        z=int(input())
        arr.append(z)
    mat.append(arr)

print("Original Matrix: ")
for i in range(0,n):
    for j in range(0,m):     
        print(mat[i][j],end=" ")
    print()

mat2=[]
print("Enter elements :")
for i in range(0,n):
    arr=[]
    for j in range(0,m):
        arr.append(0)
    mat2.append(arr)


for i in range(0,n):
        for j in range(0,m):
                mat2[j][n-1-i] =mat[i][j]

print("Matrix after rotation by 90 degree clockwise")
for i in range(0,n):
    for j in range(0,m):     
        print(mat2[i][j],end=" ")
    print()

