print("Connect 4 Game: ")
game = ["                                          "] # 42 spaces
print("This is the game's grid: ")
print(" | | | | | | | | \n | | | | | | | | \n | | | | | | | | \n | | | | | | | | \n | | | | | | | | \n | | | | | | | | \n | | | | | | | | ")


r1=[" |"," ", "|", " ", "|", " ", "|", " ", "|", " ", "|", " ", "|", " ", "|"]
r2=[" |"," ", "|", " ", "|", " ", "|", " ", "|", " ", "|", " ", "|", " ", "|"]
r3=[" |"," ", "|", " ", "|", " ", "|", " ", "|", " ", "|", " ", "|", " ", "|"]
r4=[" |"," ", "|", " ", "|", " ", "|", " ", "|", " ", "|", " ", "|", " ", "|"]
r5=[" |"," ", "|", " ", "|", " ", "|", " ", "|", " ", "|", " ", "|", " ", "|"]
r6=[" |"," ", "|", " ", "|", " ", "|", " ", "|", " ", "|", " ", "|", " ", "|"]
r7=[" |"," ", "|", " ", "|", " ", "|", " ", "|", " ", "|", " ", "|", " ", "|"]
print(r1)
print(r2)
print(r3)
print(r4)
print(r5)
print(r6)
print(r7)
player_RED = int(input("Player Red, enter your first disk: "))
if player_RED == 1 :
    r7[1] = "R"
    print(r1)
    print(r2)
    print(r3)
elif player_RED == 2 :
    r7[3] = "R"
    print(r1)
    print(r2)
    print(r3)
elif player_RED == 3 :
    r7[5] = "R"
    print(r1)
    print(r2)
    print(r3)
elif player_RED == 4 :
    r7[7] = "R"
    print(r1)
    print(r2)
    print(r3)   
elif player_RED == 5 :
    r7[9] = "o"
    print(r1)
    print(r2)
    print(r3)
elif player_RED == 6 :
    r7[11] = "R"
    print(r1)
    print(r2)
    print(r3)
elif player_RED == 7 :
    r7[13] = "R"
    print(r1)
    print(r2)
    print(r3)
    

player_BLUE = int(input("Player Blue, enter your first disk: "))