from Trees_easy.linked_binary_tree import LinkedBinaryTree as Tree
from random import sample
from copy import deepcopy


class Board:
    def __init__(self, sign=None, position=None):
        self.board = [[None for i in range(3)] for i in range(3)]
        self.last_move = (sign, position)

    def check(self):
        """
        Checks for a winner after the last move
        """
        x, y = self.last_move[1]

        if self.board[0][y] == 'X' and self.board[1][y] == 'X' and\
                self.board[2][y] == 'X':
            return True
        if self.board[0][y] == 'O' and self.board[1][y] == 'O' and\
                self.board[2][y] == 'O':
            return True

        if self.board[x][0] == 'X' and self.board[x][1] == 'X' and\
                self.board[x][2] == 'X':
            return True
        if self.board[x][0] == 'O' and self.board[x][1] == 'O' and\
                self.board[x][2] == 'O':
            return True
        if self.board[0][0] == 'X' and self.board[1][1] == 'X' and\
                self.board[2][2] == 'X':
            return True
        if self.board[0][0] == 'O' and self.board[1][1] == 'O' and\
                self.board[2][2] == 'O':
            return True
        if self.board[0][2] == 'X' and self.board[1][1] == 'X' and\
                self.board[2][0] == 'X':
            return True
        if self.board[0][2] == 'O' and self.board[1][1] == 'O' and\
                self.board[2][0] == 'O':
            return True
        return False

    def move(self, sign, position):
        if position[0] > 2 or position[1] > 2 or\
                position[0] < 0 or position[0] < 0:
            print('Wrong coordinates. Try again!')
            return None
        if self.board[position[0]][position[1]] is not None:
            print('Position already taken. Try again!')
            return None
        self.board[position[0]][position[1]] = sign
        self.last_move = (sign, position)
        return True

    def draw(self):
        """
        Shows current state of a board
        """
        for i in range(3):
            print('|', end='')
            for j in range(3):
                if self.board[i][j]:
                    print(self.board[i][j], end='|')
                else:
                    print(' ', end='|')
            print()

    def possible_moves(self):
        res = set()
        for i in range(3):
            for j in range(3):
                if not self.board[i][j]:
                    res.add((i, j))
        return res

    def is_full(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] is None:
                    return False
        return True


b = Board()
b.draw()


class Player:
    def __init__(self, sign, board):
        self.sign = sign
        self.board = board


class Human(Player):
    pass


class Bot(Player):
    def fill_tree(self, human):
        board = deepcopy(self.board)
        tree = Tree(board)

        def recurse(tree):
            possible = board.possible_moves()
            print(possible)
            if len(possible) > 1:
                left, right = sample(possible, 2)

                tree.insert_left(deepcopy(board).move(self.sign, left))
                tree.insert_right(deepcopy(board).move(self.sign, right))

                possible = board.possible_moves()
                left, right = sample(possible, 2)
                tree.insert_left(deepcopy(board).move(human.sign, left))
                tree.insert_right(deepcopy(board).move(human.sign, right))

                return recurse(tree.get_left_child()) + recurse(tree.get_right_child())

            if len(possible) == 1:
                left = list(possible)[0]
                tree.insert_left(deepcopy(board).move(self.sign, left))
                return recurse(tree.get_left_child())
            else:
                return tree

        recurse(tree)


bot = Bot('X', b)
h = Human('O', b)
bot.fill_tree(h)



def game():
    b = Board()
    sign = input('Enter your sign("X" or "O"): ')
    sign_bot = "O" if sign != "O" else "X"

    player = Player(sign, b)
    bot = Bot(sign_bot, b)


