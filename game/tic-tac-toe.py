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
        if not 0 < position[0] < 3 or not 0 < position[1] < 3:
            print('Wrong coordinates. Try again!')
            return None
        if self.board[position[0]][position[1]]:
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


b = Board()
b.draw()


def fill_tree(current_board):
    tree = Tree(current_board)
    possible = sample(current_board.possible_moves(), 2)
    if current_board.last_move[0] == 'X':
        sign = 'O'
    else:
        sign = 'X'
    b_left = deepcopy(current_board)
    b_right = deepcopy(current_board)
    b_left.move(sign, possible[0])
    b_right.move(sign, possible[1])
    tree.insert_left(b_left)
    tree.insert_right(b_right)
    print(possible)

    def recurse(left=tree.get_left_child(), right=tree.get_right_child()):
        if len(current_board.possible_moves()) < 2:
            return tree
        possible = sample(current_board.possible_moves(), 2)
        if current_board.last_move[0] == 'X':
            sign = 'O'
        else:
            sign = 'X'
        b_left = deepcopy(current_board)
        b_right = deepcopy(current_board)
        b_left.move(sign, possible[0])
        b_right.move(sign, possible[1])
        left.insert_left(b_left)
        right.insert_right(b_right)
        return recurse(left=tree.get_left_child(), right=tree.get_right_child())

    return recurse(tree)


fill_tree(b)
