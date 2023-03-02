import random

players = []
red_team = []
blue_team = []

for i in range(10):
    player = input("Nom du joueur :")
    players.append(player)

for i in range(5):
    red_player = random.choice(players)
    red_team.append(red_player)
    players.remove(red_player)

for i in range(5):
    blue_player = random.choice(players)
    blue_team.append(blue_player)
    players.remove(blue_player)

print(blue_team)
print(red_team)

