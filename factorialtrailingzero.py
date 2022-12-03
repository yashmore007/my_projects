def factorial_func(num1):
    if num1==0:
        return 0
    elif num1==1:
        return 1
    else:
        return num1*factorial_func(num1-1)        
print("enter the number you want factorial for")
no_input=int(input("enter the number here...\n"))
a=factorial_func(no_input)
print("your factorial is ",a)
a=str(a)
j=(len(a)-1)
score=0
while(a[j]=="0"):
    if a[j]=="0":
        score+=1
    j=j-1
print("trailing zeroes in factorial is ",score)    