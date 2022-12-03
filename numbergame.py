import random
a=int(input("Enter the samllest number in the range"))
b=int(input("enter the highest number in the range"))
c=random.randrange(a,b)

print("now you guess what number is selected by the computer")
i=0
while(1):
   choice_number=int(input("enter now...\n"))
   if choice_number<c:
       print("too small number is enterred")
   elif choice_number>c:
       print("too big number entered")
   elif choice_number==c:
       print("you won the game")
   i+=1

print("you have taken ",i,"chanes")