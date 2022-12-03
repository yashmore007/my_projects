print("how many numbers you want to give as input ")
print("plese type here ...\n")
loop_no=input()
i=0
while(i<int(loop_no)):
    print("enter the number you want the next pllindrome for \n")
    palli_no=input()
    if palli_no[::-1]==palli_no:
        print("you have entered pallindrome")
    else:
        j=0
        palli_no=int(palli_no)
        while(j<99999):
            (palli_no)=(palli_no)+1
            palli_no=str(palli_no)
            if palli_no[::-1]==palli_no:
                print("yes we got it your pallindrome is",palli_no)
                break
            palli_no=int(palli_no)    
        j=j+1
    i=i+1