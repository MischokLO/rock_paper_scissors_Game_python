import random

moves = ['rock', 'paper', 'scissors']


class AbstractPlayer:
    def __init__(self):
        self.my_move = None

    def move(self):
        raise "Not Implemented"

    def learn(self, their_move, my_move):
        raise "Not Implemented"


class RandomPlayer(AbstractPlayer):

    def move(self):
        move = random.choice(moves)
        return move

    def learn(self, their_move, my_move):
        pass


class ALwaysRockPlayer(AbstractPlayer):

    def move(self):
        move = "rock"
        return move

    def learn(self, their_move, my_move):
        pass


class HumanPlayer(AbstractPlayer):

    def move(self):
        move = input("Enter your move: ")
        while move not in moves:
            move = input("Invalid move, choose again: ")
        return move

    def learn(self, their_move, my_move):
        pass


class ReflectPlayer(AbstractPlayer):
    their_move = None

    def move(self):
        if self.their_move is None:
            return "rock"
        else:
            return self.their_move

    def learn(self, their_move, my_move):
        self.their_move = their_move


class CyclePlayer(AbstractPlayer):

    def move(self):
        if self.my_move is None:
            return "rock"
        elif self.my_move is "rock":
            return "paper"
        elif self.my_move is "paper":
            return "scissors"
        elif self.my_move is "scissors":
            return "rock"

    def learn(self, their_move, my_move):
        self.my_move = my_move


def beats(one, two):
    if (one == 'rock' and two == 'scissors' or
            one == 'scissors' and two == 'paper' or
            one == 'paper' and two == 'rock'):
        print('Player1 won\n')
        i = 1
        return i
    elif (one == 'scissors' and two == 'rock' or
            one == 'paper' and two == 'scissors' or
            one == 'rock' and two == 'paper'):
        print('Player2 won\n')
        i = -1
        return i
    else:
        print('Draw \n')
        i = 0
        return i


playerMappings = {
    "RandomPlayer": RandomPlayer,
    "HumanPlayer": HumanPlayer,
    "CyclePlayer": CyclePlayer,
    "ReflectPlayer": ReflectPlayer,
    "AlwaysRockPlayer": ALwaysRockPlayer
}
