import string
import random

if __name__=="__main__":
    s1=string.ascii_lowercase
    s2=string.ascii_uppercase
    s3=string.digits
    s4=string.punctuation
    
    plen=int(input("Enter passward lenght \n"))
    if plen<9:
        print("too short passward create strong one.\n")
    s=[]
    s.extend(list(s1))    
    s.extend(list(s2))    
    s.extend(list(s3))    
    s.extend(list(s4))
    
    random.shuffle(s)
    print("your passward is :")
    print("".join(s[0:plen]))    