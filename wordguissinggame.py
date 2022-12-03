import random
lst=["mango","banana","cpu","mother"]
random_word=random.choice(lst)
print(random_word)
i=0
j=0
while(i<(len(random_word))+2):
    print("choose a letter in the word")
    choose_letter=input("enter now...\n")
    for item in random_word:
        if item==choose_letter:
            print("lenght of random word is",len(random_word),"and index is ",random_word.index(item))

    print("reeamining chances are ",((len(random_word)+2))-(i+1))
    i=i+1