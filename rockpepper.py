import random
random_exp=["rock","pepper","scissor"]
random_choose=random.choice(random_exp)
input_ans=input("enter your choice\n")
if random_choose=="rock" and input_ans=="rock":
    print("no one won the game")
elif random_choose=="rock" and input_ans=="pepper":
    print("you won the game")
        
elif random_choose=="rock" and input_ans=="scissor":
    print("you lose the game")
        
elif random_choose=="pepper" and input_ans=="rock":
    print("you lose the game")
elif random_choose=="pepper" and input_ans=="pepper":
    
    print("no one won the game")
elif random_choose=="pepper" and input_ans=="scissor":
    
    print("you won the game")
elif random_choose=="scissor" and input_ans=="rock":
    
    print("you won the game")
elif random_choose=="scissor" and input_ans=="pepper":
    
    print("you lose the game")
elif random_choose=="scissor" and input_ans=="scissor":
    
    print("no one won the game")
        