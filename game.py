import random


result={
    "gp":0,
    "draw":0,
    "comp":0,
    "user":0,
}


willing=True
count=0

while(willing): 
    game=["snake","water","gun"]
    comp=random.choice(game)
    user=input("Enter your choice from Snake,Water,Gun: ")
    count+=1 
    if(comp=="snake"):
        if(user=="water"):
            print("Computer Wins")
            result.update({"comp":result["comp"]+1})
        elif(user=="snake"):
            print("Game tie")
            result.update({"draw":result["draw"]+1})
        else:
            print("User Wins")
            result.update({"user":result["user"]+1})

    elif(comp=="water"):
        if(user=="gun"):
            print("Computer Wins")
            result.update({"comp":result["comp"]+1})
        elif(user=="water"):
            print("Game tie")
            result.update({"draw":result["draw"]+1})
        else:
            print("User Wins")
            result.update({"user":result["user"]+1})

    elif(comp=="gun"):
        if(user=="snake"):
            print("Computer Wins")
            result.update({"comp":result["comp"]+1})
        elif(user=="gun"):
            print("Game tie")
            result.update({"draw":result["draw"]+1})
        else:
            print("User Wins")
            result.update({"user":result["user"]+1})
    else:
        print("wrong Choice User hahahaha.....")

    consent=input("Do U want to play Again: (y or n)")

    if(consent=='y'):
        willing=True
    else:
        willing=False

print("==================Game Summary==================")
print("Game Played: ",count)
print("User Wins: ",result["user"])
print("Computer Wiins: ",result["comp"])
print("Game Tie: ",result["draw"])

if(result["user"]>result["comp"]):
    print("User In the Game")
elif(result["user"]==result["comp"]):
    print("Game Draw")
else:
    print("Computer Win the game")
print("===============================================")
