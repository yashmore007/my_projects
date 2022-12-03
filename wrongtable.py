five_table=[5,10,15,20,25,38,35,40,45,50]
number=5
correct_table=[]
def isCorrect(table,num):
    i=1
    while(i<11):
        correct_no=num*i
        correct_table.append(correct_no)
        i+=1
isCorrect(five_table,number)
print(correct_table)
i=0
while(i<10):
   if  five_table[i]==correct_table[i]:
       print("correct table till index",i)
   else:
       print("wrong table rohan exposed")
   i+=1