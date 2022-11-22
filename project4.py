print("Enter your age or year of birth\n")
age=int(input("Enter now...\n"))
if age==0 or age>2022:
    print("you are not born yet\n")
    exit()
elif len(str(age))==2:
    print("your age will be 100 years after ",100-age,"years\n")
    print("i.e. your age will be 100 years in ",2022+(100-age),"\n")
elif len(str(age))==4:
    print("you are ",(2022-age),"years old")
    print("your age will be 100 after ",(100-(2022-age)),"years")
    print("you will be 100 year old in year",(2022+(100-(2022-age))))
print("please enter the year in which you want to know how much your age will be (optional)\n")
year_leap=int(input("enter year....\n"))
print("if you want hit 1 and if not hit 0\n")
response_user=int(input())
if year_leap<2022:
    print("invalid input\n")
elif response_user==1 and len(str(age))==2 :
    print("your age will be",age+(year_leap-2022),"\n")
elif response_user==1 and   len(str(age))==4:
    print("your age at that year will be",((2022-age)+(year_leap-2022)))
elif response_user==0:
    print("thank you visit again")
else:
    print("you have entered wrong choice")


