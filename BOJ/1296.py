name = input()
n = int(input())

name_l = name.count('L')
name_o = name.count('O')
name_v = name.count('V')
name_e = name.count('E')

teams = []
for _ in range(n):
    team_name = input()

    team_l = team_name.count('L')
    team_o = team_name.count('O')
    team_v = team_name.count('V')
    team_e = team_name.count('E')

    l = name_l + team_l
    o = name_o + team_o
    v = name_v + team_v
    e = name_e + team_e

    score = (l+o) * (l+v) * (l+e) * (o+v) * (o+e) * (v+e) % 100

    teams.append((team_name, score))

teams.sort(key=lambda x:(-x[1],x[0]))
print(teams[0][0])