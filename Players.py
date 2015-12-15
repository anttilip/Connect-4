#!/usr/bin/env python
# -*- coding: utf-8 -*-
from random import randint
from Negamax import Negamax


class HumanPlayer:
    is_ai = False

    def __init__(self, sign='X'):
        self.sign = sign

    def get_move(self, board):
        while True:
            move = raw_input()
            if self.is_valid(move, board):
                break
            print 'Please give a valid column number'

        return int(move)

    def is_valid(self, move, board):
        try:
            move = int(move)
        except ValueError:
            return False

        return 0 < move <= board.width


class AIPlayer:
    is_ai = True

    def __init__(self, sign='O'):
        self.sign = sign

    def get_move(self, board):
        print Negamax().pef(board)
        return randint(1, 7)
