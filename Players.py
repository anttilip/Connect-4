#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Negamax import Negamax


class HumanPlayer:
    is_ai = False

    def __init__(self, sign):
        self.sign = sign

    def get_move(self, board, opponent):
        while True:
            move = raw_input()
            if self.is_valid(move, board):
                break
            print 'Please give a valid column number'

        return int(move)

    @staticmethod
    def is_valid(move, board):
        try:
            move = int(move)
        except ValueError:
            return False

        return 0 < move <= board.width


class AIPlayer:
    is_ai = True

    def __init__(self, sign):
        self.sign = sign

    def get_move(self, board, opponent):
        n = Negamax(board, 4)
        move, _ = n.negamax(board, self.sign, opponent.sign)
        return move
