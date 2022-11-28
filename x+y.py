
def transform(b):
    for i in range(len(b)-1):
        if b[i]=='1':
            b[i]='0'
            if b[i+1]=='1':
               b[i+1]='0'
            else:
                b[i+1]='1'   
    return b
if __name__ =='__main__':
    a=list("000111111110011")
    print(a)
    a=transform(a.copy())
    print(a)
    