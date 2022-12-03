print("enter the number of apples you want to give harry potter\n")
n=int(input("enter now...\n"))
print("now enter the range \n")
mn=int(input("enter smaller number of range\n"))
mx=int(input("enter the bigger number of range\n"))
for item in range(mn,mx+1):
    if n%item==0:
        print(n,"is divisible by",item)
    else:
        print(n,"is not divisible by ",item)