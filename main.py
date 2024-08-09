import os
import shutil

POINTS_TARGET = 100
TERMINAL_WIDTH, _ = shutil.get_terminal_size()

os.system('clear')

print("Witaj w grze rzutki!")
print("\nWprowadź imiona graczy zatwierdzając enterem i potwierdź wpisując 'c'.", end="\n")
print("-" * TERMINAL_WIDTH)

players = []


class Player:
    def __init__(self, name):
        self.name = name
        self.points = []

    def is_winner(self):
        return sum(self.points) == POINTS_TARGET

    def add_points(self, points):
        if sum(self.points) + points > POINTS_TARGET:
            self.points.append(0)
        else:
            self.points.append(points)


def split_screen():
    print("-" * TERMINAL_WIDTH)


def round():
    for player in player_instances:
        if player.is_winner():
            continue
        else:
            print(f"Rzuca: {player.name}")
            score = input(f"{player.name} zdobył punktów: ")
            player.add_points(int(score))
            print(f"Pozostaje {POINTS_TARGET - sum(player.points)} punktów")
            split_screen()


def rounds_played():
    return max([len(player.points) for player in player_instances])


def draw_scoreboard():
    os.system('clear')
    split_screen()
    print("\t[START]", end='')
    for i in range(rounds_played()):
        print(f"\tTura {i + 1}", end='')
    for player in player_instances:
        print(f"\n{player.name}\t{POINTS_TARGET}\t", end='')
        for j in range(len(player.points)):
            print(POINTS_TARGET - sum(player.points[:j + 1]), end='\t')
    print("\n")
    split_screen()


def all_players_finished():
    return all([player.is_winner() for player in player_instances])


try:
    while True:
        name = input("Wprowadź imie gracza: ")
        if name.lower() == "c":
            break
        players.append(name.lower())
    os.system('clear')
    player_instances = [Player(player.capitalize()) for player in players]
    draw_scoreboard()

    while True:
        if all_players_finished():
            break
        else:
            round()
            draw_scoreboard()

    print("Koniec gry, GG!!!")


except KeyboardInterrupt:
    print("\nExiting...")