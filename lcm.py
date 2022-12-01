
def find_lcm(num1,num2,maximum):
    j=0
    while(j<99999):
        if (maximum%num1==0) and (maximum%num2==0):
            return maximum
            break
    j=j+1
    maximum+=1
 
print("Enter the two number you want lcm of")
num1=int(input("Enter no 1\n"))
num2=int(input("Enter no 2\n"))
maximum=max(num1,num2)
result=find_lcm(num1,num2,maximum)
print(f"lcm of given two numbers is {result}")
