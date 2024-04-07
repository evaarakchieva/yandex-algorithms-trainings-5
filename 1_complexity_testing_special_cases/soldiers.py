def fight(x, y, p):
    min_coefficient = 1.45
    max_coefficient = 1.8
    step = 0.0003
    strategy = []

    for coefficient in [rounds * step for rounds in range(int(min_coefficient/step), int(max_coefficient/step))]:
        enemies = 0
        my_army = x
        enemy_base = y
        rounds = 0
        if p >= my_army and my_army < enemy_base and (enemy_base - my_army + p) / my_army > coefficient:
            strategy.append(999999)
            continue

        while True:
            rounds += 1
            test = False
            if (enemy_base + p) / my_army <= coefficient:
                test = True

            if test:
                if enemy_base > 0 and enemy_base >= my_army:
                    enemy_base -= my_army
                elif enemy_base < my_army:
                    enemies -= (my_army - enemy_base)
                    enemy_base = 0
                    if enemies < 0:
                        enemies = 0
            else:
                if enemies <= my_army:
                    enemy_base -= (my_army - enemies)
                    enemies = 0
                else:
                    enemies -= my_army
            if enemies > 0:
                my_army -= enemies
            if enemy_base > 0:
                enemies += p
            if my_army <= 0:
                rounds = 999999
                break
            if enemy_base <= 0 and enemies <= 0:
                break
        strategy.append(rounds)

    ans = min(strategy)
    if ans == 999999:
        print(-1)
    else:
        print(ans)

    return


input_x = int(input())
input_y = int(input())
input_p = int(input())
fight(input_x, input_y, input_p)
