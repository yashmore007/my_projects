
def matrix(m,n):
    out=[]
    for i in range(m):
        row=[]
        for j in range(n):
            inp=int(input(f"enter number at {i}{j}"))
            row.append(inp)
        out.append(row)
    return out  

def summatri(A,B):
    outp=[]
    for i in range(len(A)):
        row=[] 
        for j in range(len(A[0])):
            row.append(A[i][j]+B[i][j])
        outp.append(row) 
    return outp        
m=int(input("Enter number of rows\n"))
n=int(input("Enter the number of columns\n"))

print("enter the matrix A")
A=matrix(m,n)
print(A)

print("enter the matrix B")
B=matrix(m,n)
print(B)

print("The sum of matrix is :")
sum=summatri(A,B)
print(sum)