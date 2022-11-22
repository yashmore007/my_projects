secure=(('s','$'),('and','&'),('a','@'),('o','0'),('i','1')
        ,('I','|'))
def securePassward(passward):
    for a,b in secure:
        passward=passward.replace(a,b)
    return passward    
if __name__ =="__main__":
    passward=input("enter your passward\n")
    passward=securePassward(passward)
    print(f"your passward is {passward}")