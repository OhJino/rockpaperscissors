#!/usr/bin/env python3

import random
moves = ['rock', 'paper', 'scissors']


class Player:
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        self.my_move = my_move
        self.their_move = their_move


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class RandomPlayer(Player):
    def move(self):
        return (random.choice(moves))


class HumanPlayer(Player):
    def move(self):
        human_move = ''
        while ((human_move != "rock") and (human_move != "paper") and
               (human_move != "scissors")):
            human_move = input("Rock, paper, scissors? ('-1' to quit) > ")
            if "-1" in human_move:
                break
        else:
            return(human_move)


class ReflectPlayer(Player):
    def __init__(self):
        self.their_move = ""

    def move(self):
        while not self.their_move:
            return (random.choice(moves))
        else:
            return(self.their_move)


class CyclePlayer(Player):
    def __init__(self):
        self.my_move = ""

    def move(self):
        while self.my_move is not True:
            return (random.choice(moves))
        else:
            next_move = []
            for move in moves:
                if move != self.my_move:
                    next_move.append(move)
            return(random.choice(next_move))


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.p1.score = 0
        self.p2.score = 0
        self.p1.status = ''

    def play_game(self):
        print("Game start!")
        round_count = input("How many rounds would you like to play? > ")
        round = 0
        while round < int(round_count):
            round += 1
            print(f"---- Round {round} ----")
            self.play_round()
            if (self.p1.status == '-1'):
                break
        print(f"GAME OVER!\nThe game ended with a score of:   ",
              self.p1.score, " - ", self.p2.score,
              f"   {self.winner_of_game().upper()} WON THE GAME!")

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        if move1 is None:
            self.p1.status = '-1'
            return
        print(f"You played {move1}  \nYour opponent played {move2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        if beats(move1, move2) is True:
            self.p1.score = self.p1.score + 1
            print("You won this round!")
        elif beats(move2, move1) is True:
            self.p2.score = self.p2.score + 1
            print("Player 2 won this round")
        else:
            print("TIE")
        print("The score is ", self.p1.score, " - ", self.p2.score)

    def winner_of_game(self):
        winner = ''
        if self.p1.score > self.p2.score:
            winner = "You"
        elif self.p1.score < self.p2.score:
            winner = "Player Two"
        else:
            winner = "Nobody"
        return(winner)


if __name__ == '__main__':
    game = Game(HumanPlayer(), ReflectPlayer())
    game.play_game()
