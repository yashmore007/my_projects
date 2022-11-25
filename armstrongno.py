

sum=0
arm_no=int(input("enter the number : \n"))
len_no=len(str(arm_no))
arm_no=str(arm_no)
for item in arm_no:
    sum=sum+int(item)**len_no
arm_no=int(arm_no)
if (sum==arm_no):
    print("input nnumber is armstrong no")
else:
    print("input number is not arm strong no")      