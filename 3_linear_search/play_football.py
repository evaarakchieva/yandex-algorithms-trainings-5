def add_goal_to_player(player, minute, goals_per_player, team):
    if player not in goals_per_player:
        goals_per_player[player] = {
            "goals": 0,
            'goal_minute': [0 for _ in range(91)],
            "score": 0,
            'team': team,
        }
    goals_per_player[player]['goals'] += 1
    goals_per_player[player]['goal_minute'][minute] += 1


def add_match_to_team(team, goals, goals_per_team):
    if team not in goals_per_team:
        goals_per_team[team] = {
            "games": 0,
            "goals": 0,
            "score": 0,
        }
    goals_per_team[team]['goals'] += goals
    goals_per_team[team]['games'] += 1


def add_score_to_sys(info, goals_per_team, goals_per_player):
    _, player, team_name = info[0]
    goals_per_team[team_name]['score'] += 1
    goals_per_player[player]['score'] += 1


def add_match_to_sys(text_fragment, goals_per_team, goals_per_player):
    words = text_fragment[0].split()
    score_1, score_2 = list(map(int, words[-1].split(':')))
    team_1, team_2 = [], []
    first_team_is_added = False
    for word in words[:-1]:
        if word == '-':
            first_team_is_added = True
        else:
            team_1.append(word) if not first_team_is_added else team_2.append(word)

    team_1 = '_'.join(team_1)
    team_2 = '_'.join(team_2)
    add_match_to_team(team_1, score_1, goals_per_team)
    add_match_to_team(team_2, score_2, goals_per_team)
    info = []
    for i, line in enumerate(text_fragment[1:]):
        words = line.split()
        player = '_'.join(words[:-1])
        minute = int(words[-1][:-1])
        team_name = team_2 if i >= score_1 else team_1
        info.append([minute, player, team_name])
        add_goal_to_player(player, minute, goals_per_player, team_name)
    info.sort()
    if info:
        add_score_to_sys(info, goals_per_team, goals_per_player)


def total_goals_for(line, goals_per_team):
    team_name = line[16:]
    words = team_name.split()
    team_name = '_'.join(words)
    if team_name in goals_per_team:
        return goals_per_team[team_name]['goals']
    return 0


def score_opens_by(line, goals_per_team, goals_per_player):
    name = line[15:]
    words = name.split()
    name = '_'.join(words)
    if name in goals_per_team:
        return goals_per_team[name]['score']
    if name in goals_per_player:
        return goals_per_player[name]['score']
    return 0


def total_goals_by(line, goals_per_player):
    player_name = line[15:]
    words = player_name.split()
    player_name = '_'.join(words)
    if player_name in goals_per_player:
        return goals_per_player[player_name]['goals']
    return 0


def mean_goals_per_game_for(line, goals_per_team):
    team_name = line[24:]
    words = team_name.split()
    team_name = '_'.join(words)
    mean_goals = goals_per_team[team_name]['goals'] / goals_per_team[team_name]['games']
    return mean_goals


def mean_goals_per_game_by(line, goals_per_team, goals_per_player):
    player_name = line[23:]
    words = player_name.split()
    player_name = '_'.join(words)
    team_name = goals_per_player[player_name]['team']
    mean_goals_by = goals_per_player[player_name]['goals'] / goals_per_team[team_name]['games']
    return mean_goals_by


def goals_on_minute(line, goals_per_player):
    request = line[16:]
    words = request.split('by')
    minute = int(words[0])
    player_name = '_'.join(words[1].split())
    if player_name in goals_per_player:
        return goals_per_player[player_name]['goal_minute'][minute]
    return 0


def goals_on_first(line, goals_per_player):
    min_and_user_name = line[15:]
    words = min_and_user_name.split('minutes by')
    minute = int(words[0])
    player_name = '_'.join(words[1].split())
    if player_name in goals_per_player:
        goals = sum(goals_per_player[player_name]['goal_minute'][:minute + 1])
        return goals
    return 0


def goals_on_last(line, goals_per_player):
    max_minutes = 91
    request = line[14:]
    words = request.split('minutes by')
    minute = int(words[0])
    player_name = '_'.join(words[1].split())
    if player_name in goals_per_player:
        goals = sum(goals_per_player[player_name]['goal_minute'][max_minutes - minute:])
        return goals
    return 0


def process_request(line, goals_per_team, goals_per_player):
    if line.startswith('Total goals for'):
        return total_goals_for(line, goals_per_team)
    if line.startswith('Score opens by'):
        return score_opens_by(line, goals_per_team, goals_per_player)
    if line.startswith('Total goals by'):
        return total_goals_by(line, goals_per_player)
    if line.startswith('Mean goals per game for'):
        return mean_goals_per_game_for(line, goals_per_team)
    if line.startswith('Mean goals per game by'):
        return mean_goals_per_game_by(line, goals_per_team, goals_per_player)
    if line.startswith('Goals on minute'):
        return goals_on_minute(line, goals_per_player)
    if line.startswith('Goals on first'):
        return goals_on_first(line, goals_per_player)
    if line.startswith('Goals on last'):
        return goals_on_last(line, goals_per_player)


def solve():
    with open('input.txt', 'r') as f:
        text = f.read()
    lines = text.split('\n')
    goals_per_team = dict()
    goals_per_player = dict()
    result = []
    k = None
    for index, line in enumerate(lines):
        if line:
            if any(line.startswith(start) for start in ['Total', 'Mean', 'Goals', 'Score']):
                req = process_request(line, goals_per_team, goals_per_player)
                result.append(req)
            elif k is None or index >= k:
                words = line.split()
                score_1, score_2 = list(map(int, words[-1].split(':')))
                k = index + score_1 + score_2 + 1
                add_match_to_sys(lines[index: k], goals_per_team, goals_per_player)
    print('\n'.join(str(res) for res in result))
    return


solve()
