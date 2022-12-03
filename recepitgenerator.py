sum=0
while(True):
    print("enter the price of items after press q ")
    userInput=input("Enter here...\n")
    if (userInput!='q'):
        sum=sum +int(userInput)
        print("total so far is ",sum)
    else:
        print(f"your total value is {sum}\n thanks for shoping with us")
        break     