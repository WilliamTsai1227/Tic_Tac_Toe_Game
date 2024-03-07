# Display the grid            #做一個可以顯示九宮格的function
# Accpet user input           #做一個user input function
                              #做一個會不斷變動O X的function
# Update the game grid        #做一個更新九宮格的function
# Game win-checking algorithm #做一個輸贏確認的function
# Improving game mechanism    #改進程式
row1 = [' ',' ',' '] #user_choice 1 2 3 # index 0,1,2
row2 = [' ',' ',' '] #user_choice 4 5 6 # index 0,1,2   # 4%3=1 ,5%3=2 ,6%3=0 #position(-1) 0 ,1 ,-1
row3 = [' ',' ',' '] #user_choice 7 8 9 # index 0,1,2
prompt = "User1:O ; User2:X"
counter = -1

def display():
    print(prompt)
    print(row1)
    print(row2)
    print(row3)

def user_choice():
    choice = input("Please enter a number (1-9): ")
    while not choice.isdigit() or (int(choice) not in range(1,10)):
        if not choice.isdigit():
            print("Input is invalid")
        else:
            print("Your choice is not within the range of 1-9")
        choice = input("Please enter a number (1-9): ")
    return int(choice)

def get_currentSymbol():
    global counter
    symbol_list = ["O","X"]
    counter += 1
    return symbol_list[counter%2]
 
def update_table():
    index = user_choice()
    if index in range(1,4):
        if row1[index-1] == " ":
            row1[index-1] = get_currentSymbol()
            return True
        else:
            return False
    elif index in range(4,7):
        if row2[index%3 -1] == " ":
            row2[index%3 -1] = get_currentSymbol()
            return True
        else:
            return False
    elif index in range(7,10):
        if row3[index%3 -1] == " ":
            row3[index%3 -1] = get_currentSymbol()
            return True
        else:
            return False
        
def win_or_lose():
    empty_set = {" "}
    setRow1 = set(row1)
    setRow2 = set(row2)
    setRow3 = set(row3)
    decision = False
    if empty_set.issubset(setRow1) == False:
        if row1[0]==row1[1] and row1[1]==row1[2]:
            display()
            if row1[0]=="O":
                print("User_1 win,congratulate!")
            else:
                print("User_2 win,congratulate!")
            return True
    if empty_set.issubset(setRow2) == False:
        if row2[0]==row2[1] and row2[1]==row2[2]:
            display()
            if row2[0]=="O":
                print("User_1 win,congratulate!")
            else:
                print("User_2 win,congratulate!")
            return True
    if empty_set.issubset(setRow3) == False:
        if row3[0]==row3[1] and row3[1]==row3[2]:
            display()
            if row3[0]=="O":
                print("User_1 win,congratulate!")
            else:
                print("User_2 win,congratulate!")
            return True
    for i in range(3):
        if row1[i] != " " and row2[i] != " " and row3[i] != " ":   
            if row1[i] == row2[i] and row2[i] == row3[i]:
                display()
                if row1[i] == "O":
                        print("User_1 win,congratulate!")
                else:
                    print("User_2 win,congratulate!")
                return True
    if row1[0] != " " and row2[1] != " " and row3[2] != " ":   
        if row1[0] == row2[1] and row2[1] == row3[2]:
            display()
            if row1[0] == "O":
                print("User_1 win,congratulate!")
            else:
                print("User_2 win,congratulate!")
            return True
    if row1[2] != " " and row2[1] != " " and row3[0] != " ":   
        if row1[2] == row2[1] and row2[1] == row3[0]:
            display()
            if row1[2] == "O":
                print("User_1 win,congratulate!")
            else:
                print("User_2 win,congratulate!")
            decision = True
            return True
    if counter == 8 :
        print("Tie game.")
        display()
        return True                    

def run_game():
    while True:
        display()
        while True:
            if update_table():
                break
            else:
                print("Wrong position to put your choice")
        if win_or_lose():
            return

run_game()