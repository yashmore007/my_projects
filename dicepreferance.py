import random
print("for normal dice press 1 \n for dice for max 2 press 2 \n for dice for max 6 press 3 ")
choice_dice=int(input("enter now...\n"))

if choice_dice==1:
    i=0
    while(i<9999):
        dice_number=random.randrange(0,7)
        print("do you want to roll the dice\n if yes hit 1 if no hit 0")
        n=int(input("Enter now...\n"))
        if n==1:
            print("your dice gave ",dice_number)
        elif n==0:
            exit()
        else:
            print("you have entered wrong choice")
        i+=1      
elif choice_dice==2:
    lst_dice=[2,1,2,3,2,4,2,5,2,6,2]
    j=0
    while(j<9999):
        random_choice=random.choice(lst_dice)
        print("do you want to roll the dice\n if yes hit 1 if no hit 0")
        n1=int(input("Enter now...\n"))
        if n1==1:
            print("your dice gave ",random_choice)
        elif n1==0:
            exit()
        else:
            print("you have entered wrong choice")          
elif choice_dice==3:
    lst_dice_six=[6,1,2,3,6,4,6,5,6,6,6]
    j=0
    while(j<9999):
        random_choice_six=random.choice(lst_dice_six)
        print("do you want to roll the dice\n if yes hit 1 if no hit 0")
        n2=int(input("Enter now...\n"))
        if n2==1:
            print("your dice gave ",random_choice_six)
        elif n2==0:
            exit()
        else:
            print("you have entered wrong choice")   
else:
    print("wrong choice")            