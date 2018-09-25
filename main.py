from Game import *
from Player import *

PlayerChoices = ["RandomPlayer", "HumanPlayer",
                 "CyclePlayer", "AlwaysRockPlayer", "ReflectPlayer"]

if __name__ == '__main__':
    p1 = input("Select a Player from HumanPlayer, RandomPlayer, CyclePlayer, AlwaysRockPlayer"
               "or ReflectPlayer: ")
    print("\n")
    while p1 not in PlayerChoices:
        p1 = input("Invalid Playerchoise, choose a valid one from HumanPlayer,"
                   " RandomPlayer, CyclePlayer, AlwaysRockPlayer or ReflectPlayer: ")
        print("\n")
    p2 = input("Select a second Player from HumanPlayer, RandomPlayer,"
               "CyclePlayer, AlwaysRockPlayer or ReflectPlayer: ")
    print("\n")
    while p2 not in PlayerChoices:
        p2 = input("Invalid Playerchoise, choose a valid one from HumanPlayer,"
                   " RandomPlayer, CyclePlayer, AlwaysRockPlayer or ReflectPlayer: ")
        print("\n")
    game = Game(playerMappings[p1](), playerMappings[p2]())
    game.play_game()
