
# __________________Tasks_________________

'''
Write a Python program to take team size from the user and take their names.
Your job is to split in approximate 2 halves only such that members of TeamA shall not reflect in TeamB

Sample Shown in Folder

'''



import random

num1=int(input("Pls enter team size: "))
main_team=[]
team1=[]
team2=[]

# input team names by user choice:
print("Pls enter team member's name one by one and all should be unique: ")
i=0
while(i<num1):
    name=input(f"Name {i+1}: ")
    if name in main_team:
        print("Pls enter unique name, this name already exists in team.")
    elif name=="" or name==" ":
        print("Pls enter proper name, it should not be blank.")
    else:
        main_team.append(name)
        i=i+1
print("\nName entered in team : ",main_team)

# selecting random team 1
team1=random.sample(main_team,int(len(main_team)/2))

# selecting team 2 not in team 1
for i in main_team:
    if i not in team1:
        team2.append(i)

print("Team1 : ",team1)
print("Team2 : ",team2)

