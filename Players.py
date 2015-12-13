#!/usr/bin/env python
# -*- coding: utf-8 -*-
from random import randint


class HumanPlayer():
    is_ai = False

    def __init__(self, sign='X'):
        self.sign = sign

    def get_move(self, board):
        self.board = board

        while True:
            move = raw_input()
            if self.is_valid(move):
                break
            print 'Please give a valid column number'

        return int(move)

    def is_valid(self, move):
        try:
            move = int(move)
        except:
            return False

        return move > 0 and move <= self.board.width


class AIPlayer():
    is_ai = True

    def __init__(self, sign='O'):
        self.sign = sign
        

    def get_move(self, board):
        return randint(1, 7)
