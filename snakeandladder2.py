import random

players = ["Player1","Player2","Player3","Player4"]

dice_roll_history = {player:[] for player in players}
position_history = {player :[] for player in players}

current_position = {player:0 for player in players}

winner = None

while winner is None:
    for player in players:
        dice_number = random.randint(1,6)
        dice_roll_history[player].append(str(dice_number))

        new_pos = current_position[player] + dice_number

        if new_pos == 16:
            position_history[player].append(str(new_pos))
            winner = player
            break
        
        elif new_pos > 16:
            position_history[player].append(str(current_position[player]))
            continue

        else:
            position_history[player].append(str(new_pos))
            current_position[player] = new_pos



print(f"{'Player':<12} {'Dice Roll History':<30} {'Position History':<30} {'Win Status'}")
for player in players:
    dice_history = ",".join(dice_roll_history[player])
    position_history_str = ",".join(position_history[player])
    winner_flag = 1 if winner == player else 0
    print(f"{player:<12} {dice_history:<30} {position_history_str:<30} {winner_flag}")




