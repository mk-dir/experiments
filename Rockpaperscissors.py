import random

moves=("R","P","S")
loopcontrol=1

best_of=int(input("Decide game after how many trials?"))
player_one_win_counter=0
player_two_win_counter=0
tie=0

game_state=[0,0]

#function to randomly generate a move for each player when called
def move():
    return random.choice(moves)

while loopcontrol<=best_of:
    a=move()
    b=move()

    game_state[0]=a
    game_state[1]=b

    print("Game State:",game_state)

    if game_state==['R','S'] or game_state==['P','R'] or game_state==['S','P']:
        player_one_win_counter+=1
        loopcontrol += 1
        print("Abigail Wins")

    elif game_state == ['R', 'P'] or game_state == ['P', 'S'] or game_state == ['S', 'R']:
        player_two_win_counter += 1
        loopcontrol += 1
        print("Ben Wins")

    else:
        tie+=1
        loopcontrol+=1
        print("It's a tie")

if player_one_win_counter<player_two_win_counter:
    print("Ben is the Overall winner")
    print("Wins(",player_two_win_counter,"/",player_one_win_counter,")")

elif player_one_win_counter>player_two_win_counter:
    print("Abigail is the overall Winner")
    print ( "Wins(", player_one_win_counter, "/", player_two_win_counter, ")" )
elif player_two_win_counter==player_one_win_counter:
    print("No winner, Ties")

print("Abigail:",player_one_win_counter)
print("p2:",player_two_win_counter)
print("Ties:",tie)