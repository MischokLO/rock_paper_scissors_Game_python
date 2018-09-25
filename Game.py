import Player
import sys


class Game():

    endresult = 0
    score1 = 0
    score2 = 0

    def __init__(self, p1, p2):

        self.p1 = p1
        self.p2 = p2

    def play_round(self):

        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        Result = Player.beats(move1, move2)
        if Result is 1:
            self.score1 += 1
            print(f"        Score\n Player 1 | Player 2\n    {self.score1}           {self.score2}\n")
        elif Result is -1:
            self.score2 += 1
            print(f"        Score\n Player 1 | Player 2\n    {self.score1}           {self.score2}\n")
        else:
            print(f"        Score\n Player 1 | Player 2\n    {self.score1}           {self.score2}\n")
        self.endresult += Result
        self.p1.learn(move1, move2)
        self.p2.learn(move1, move2)
        if self.endresult is 3:
            print("Player1 won the Match!" + "\n" + "Game over!")
            sys.exit()
        elif self.endresult is -3:
            print("Player2 won the Match!" + "\n" + "Game over!")
            sys.exit()
        else:
            pass

    def play_game(self):

        print("Game start!")
        round = 1
        while True:
            print(f"Round {round} :")
            self.play_round()
            round += 1
