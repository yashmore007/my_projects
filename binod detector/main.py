import os
def binod_detect(filename):
    with open(filename,"r") as f:
       content=f.read()
       if "binod" in content.lower():
           return True
       else:
           return False
score=0    
list1=os.listdir()
for item in list1:
    if item.endswith("txt"):
        print(f"detecting binod in { item }")
        flag=binod_detect(item)
        if (flag):
            print(f"binod found in {item}")
            score+=1
        else:
            print(f"binod not found in{item}")
print("binod detection done")
print(f"{score} binod files are found ")            
                
        