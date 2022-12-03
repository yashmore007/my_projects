import random
random_choose=random.randrange(100,200)
score=0
score1=0
i=0
while(i<9999):
    player1=input("player 1 = Enter the number you want to guess\n")
    player2=input(" player2 = Enter the number you want to guess\n")
    random_choose=str(random_choose)
    for item in random_choose:
        for item1 in player1:
            if item==item1:
              score+=1
              a=random_choose.index(item)
              print("you found this",a,"index and number is ",item1)
    for item in random_choose:
        for item1 in player2:
            if item==item1:
               score1+=1
               b=random_choose.index(item)
               print("you found this",b,"index and number is ",item1)
    if score==3 and score1==3:
        exit()
    i+=1            

