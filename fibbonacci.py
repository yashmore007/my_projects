def ric_fibbo(num):
    if num==0:
        return 0
    elif num==1:
        return 1
    else:
        return ric_fibbo(num-1)+ric_fibbo(num-2)

def iet_fibbo(num):
    prev_no=0
    current_no=1
    for i in range(1,num):
        prev_prev_no=prev_no
        prev_no=current_no
        current_no=prev_no+prev_prev_no
    return current_no

if __name__=='__main__':
    num=int(input("Enter your number"))
    print("fib number using riccurssive approach",ric_fibbo(num))
    print("fib using iterative approach",iet_fibbo(num))