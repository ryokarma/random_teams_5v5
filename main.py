import random

def teams_league_of_legends():

    players = []
    red_team = []
    blue_team = []
    roaster_red = {"Toplaner": None, "Midlaner": None, "ADC": None, "Support": None, "Jungler": None}
    roaster_blue = {"Toplaner": None, "Midlaner": None, "ADC": None, "Support": None, "Jungler": None}


    for i in range(10):
        player = input("Nom du joueur :")
        players.append(player)

    for i in range(5):
        red_player = random.choice(players)
        red_team.append(red_player)
        players.remove(red_player)
    roaster_red["Toplaner"] = red_team[0]
    roaster_red["Midlaner"] = red_team[1]
    roaster_red["ADC"] = red_team[2]
    roaster_red["Support"] = red_team[3]
    roaster_red["Jungler"] = red_team[4]

    for i in range(5):
        blue_player = random.choice(players)
        blue_team.append(blue_player)
        players.remove(blue_player)
    roaster_blue["Toplaner"] = blue_team[0]
    roaster_blue["Midlaner"] = blue_team[1]
    roaster_blue["ADC"] = blue_team[2]
    roaster_blue["Support"] = blue_team[3]
    roaster_blue["Jungler"] = blue_team[4]


    print(blue_team)
    print(red_team)
    print(roaster_red)
    print(roaster_blue)


def teams_overwatch():

    players = []
    red_team = []
    blue_team = []
    roaster_red = {"Tank": None, "DPS1": None, "DPS2": None, "Healer1": None, "Healer2": None}
    roaster_blue = {"Tank": None, "DPS1": None, "DPS2": None, "Healer1": None, "Healer2": None}


    for i in range(10):
        player = input("Nom du joueur :")
        players.append(player)

    for i in range(5):
        red_player = random.choice(players)
        red_team.append(red_player)
        players.remove(red_player)
    roaster_red["Tank"] = red_team[0]
    roaster_red["DPS1"] = red_team[1]
    roaster_red["DPS2"] = red_team[2]
    roaster_red["Healer1"] = red_team[3]
    roaster_red["Healer2"] = red_team[4]

    for i in range(5):
        blue_player = random.choice(players)
        blue_team.append(blue_player)
        players.remove(blue_player)
    roaster_blue["Tank"] = blue_team[0]
    roaster_blue["DPS1"] = blue_team[1]
    roaster_blue["DPS2"] = blue_team[2]
    roaster_blue["Healer1"] = blue_team[3]
    roaster_blue["Healer2"] = blue_team[4]


    print(blue_team)
    print(red_team)
    print(roaster_red)
    print(roaster_blue)


#def teams_by_game():
def teams_by_number():
    # Initialisation des listes
    players = []
    teams = []

    # Saisie du nombre de joueurs et d'équipes
    player_number = int(input("Combien de joueurs êtes-vous ? "))
    team_number = int(input("Combien d'équipes voulez-vous ? "))

    # Calcul du nombre de joueurs par équipe
    players_per_team = player_number // team_number

    # Saisie des noms des joueurs
    for i in range(player_number):
        player = input(f"Nom du joueur {i + 1} : ")
        players.append(player)

    # Création des équipes et attribution des joueurs
    for i in range(team_number):
        team = []
        for j in range(players_per_team):
            # Sélection aléatoire d'un joueur
            player = random.choice(players)
            team.append(player)
            players.remove(player)  # Suppression du joueur sélectionné de la liste des joueurs restants
        teams.append(team)

    # Affichage des équipes
    for i, team in enumerate(teams):
        print(f"Equipe {i + 1} : {team}")


print("1 - Manuel \n2 - Overwatch \n3 - League of Legends")
choice = input("Quel mode de jeu désirez-vous ?")
if choice == "1":
    teams_by_number()
elif choice == "2":
    teams_overwatch()
elif choice == "3":
    teams_league_of_legends()
else:
    print("Vous n'avez pas tapé le chiffre du mode de jeu désiré, espèce de gros naze. Merci de relancer le programme.")