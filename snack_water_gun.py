import random
def gamWin(comp, your):
    #when com and you Chose same Thing Then math is tie 
    if comp == your:
        return None
    
# All Posiblities If omputer chose  "S"
    elif comp =="s":
        if your == "w":
            return False
        elif your =="g":
            return True
# All Posiblities If omputer chose  "w"
    elif comp =="w":
        if your == "g":
            return False
        elif your =="s":
            return True
# All Posiblities If omputer chose  "g"
    elif comp =="g":
        if your == "s":
            return False
        elif your =="w":
            return True
        
print("Com Turn : Snack(s) Water (w) or Gun(g)?")
# Random Number Gunrator 
randNO = random.randint(1,3)
if randNO ==1:
    comp = "s"
elif randNO ==2:
    comp = "w"
elif randNO ==3:
    comp = "g"
# User Input 
your = input("Your Turn :Snack(s) Water (w) or Gun(g)?")
a = gamWin(comp,your)

# 
# 
print(f"Computer Choos {comp}")
print(f"You  Choose {your}")
if a == None:  
    print("Game is tie")
elif a:
    print("you Win")
else:
    print("you LOOS!  Please Try Again!")


