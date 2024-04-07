g1_1, g2_1 = map(int, input().split(':'))
g1_2, g2_2 = map(int, input().split(':'))
home_game = int(input())

total_g1 = g1_1 + g1_2
total_g2 = g2_1 + g2_2

away_g1 = g1_2 if home_game == 1 else g1_1
goals_to_win = 0

if (total_g1 == total_g2 and away_g1 > g2_2 and home_game == 2) or total_g1 > total_g2 or (total_g1 == total_g2 and away_g1 > g2_1 and home_game == 1):
    goals_to_win = 0
elif total_g1 == total_g2:
    goals_to_win = 1
else:
    if home_game == 1:
        goals_to_win = total_g2 - total_g1
        if g1_2 + goals_to_win > g2_1:
            pass
        else:
            goals_to_win += 1
    else:
        if away_g1 <= g2_2:
            goals_to_win = total_g2 - total_g1 + 1
        else:
            goals_to_win = total_g2 - total_g1

print(goals_to_win)
