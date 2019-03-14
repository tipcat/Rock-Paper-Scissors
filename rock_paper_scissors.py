import random
import string

moves = ['rock', 'paper', 'scissors']


class Player:
    def move(self):
        return moves[0]

    def learn(self, their_move):
        pass


class HumanPlayer(Player):
    def move(self):
        human_move = ""
        while human_move == "":
            human_move = str.lower(input("Rock, paper, scissors? > "))
            if human_move not in moves:
                print("You must play rock, paper or scissors. Try again:\n")
                human_move = ""
            else:
                return human_move


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


class ReflectPlayer(Player):
    def __init__(self):
        self.next_move = ""

    def move(self):
        if self.next_move == "":
            return moves[0]
        else:
            return self.next_move

    def learn(self, their_move):
        self.next_move = their_move


class CyclePlayer(Player):
    def __init__(self):
        self.next_move = ""

    def move(self):
        if self.next_move == "":
            return moves[0]
        else:
            return self.next_move

    def learn(self, my_move):
        if my_move == moves[0]:
            self.next_move = moves[1]

        elif my_move == moves[1]:
            self.next_move = moves[2]

        else:
            self.next_move = moves[0]


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.num_games = 1
        self.p1_score = 0
        self.p2_score = 0

    def play_round(self):

        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")

        if isinstance(self.p1, ReflectPlayer):
            self.p1.learn(move2)
        if isinstance(self.p1, CyclePlayer):
            self.p1.learn(move1)

        if beats(move1, move2):
            self.p1_score += 1
            print("** PLAYER ONE WINS**")
            print(f"SCORE: Player one {self.p1_score}")
            print(f"Player two {self.p2_score}\n")

        elif beats(move2, move1):
            self.p2_score += 1
            print("** PLAYER TWO WINS**")
            print(f"SCORE: Player one {self.p1_score}")
            print(f"Player two {self.p2_score}\n")

        else:
            print("** TIE **")
            print(f"SCORE: Player one {self.p1_score}")
            print(f"Player two {self.p2_score}\n")

    def play_game(self):
        if self.num_games == 1:
            self.p1 = RandomPlayer()
            self.p2 = RandomPlayer()
        if self.num_games == 2:
            self.p1 = Player()
            self.p2 = HumanPlayer()
        if self.num_games == 3:
            self.p1 = RandomPlayer()
            self.p2 = HumanPlayer()
        if self.num_games == 4:
            self.p1 = ReflectPlayer()
            self.p2 = HumanPlayer()
        if self.num_games == 5:
            self.p1 = CyclePlayer()
            self.p2 = HumanPlayer()

        for round in range(6):
            print(f"Round {round + 1} --")
            self.play_round()
        print("Game over!")
        if self.p1_score > self.p2_score:
            print("PLAYER ONE WINS THE GAME!\n")
        elif self.p2_score > self.p1_score:
            print("PLAYER TWO WINS THE GAME!\n")
        else:
            print("THE GAME ENDS IN A TIE!\n")
        self.num_games += 1
        self.p1_score = 0
        self.p2_score = 0


if __name__ == '__main__':
    game = Game(Player(), Player())

    print("Rock Paper Scissors!")
    print("Each game will have 6 rounds\n")
    print(f"Game# {game.num_games}: Random player demonstration")
    game.play_game()

    print(f"Game {game.num_games}: Your play vs. a simple computer")
    game.play_game()

    print("That was easy, no? Let's try a real game!")
    print(f"Game {game.num_games}: Your play vs. computer playing random move")
    game.play_game()

    print("Groovy! Let's try something different")
    print(f"Game {game.num_games}")
    game.play_game()

    print("And now for the concluding game, also different")
    print(f"Game {game.num_games}")
    game.play_game()
