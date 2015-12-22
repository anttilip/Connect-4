#!/usr/bin/env python
# -*- coding: utf-8 -*-
from termcolor import colored   # possibly remove for compatibility


class Board:
    """Game board for Connect 4"""
    def __init__(self, width=7, height=6):
        self.width = width
        self.height = height
        self.board = self.build_board(width, height)
        self.undo_stack = []

    def build_board(self, width, height):
        return [[' ' for x in range(width)] for y in xrange(height)]

    def place_piece(self, move, curr_sign):
        for row in reversed(self.board):
            if row[move-1] == ' ':
                row[move-1] = curr_sign
                self.undo_stack.append(move - 1)
                return True

        print 'Not allowed'
        return False

    def is_gameover(self, curr_sign, opponent_sign):
        for indexes in self.segment_indexes():

            # indexes contains four board indexes as tuples
            segment = ''.join([self.board[index[0]][index[1]] for index in indexes])

            if segment == 4 * curr_sign:
                return True, curr_sign
            elif segment == 4 * opponent_sign:
                return True, opponent_sign

            if not self.is_legal_moves_left():
                # If tie game, no winner is returned
                return True, None

        # If game is not over, no winner is returned
        return False, None

    def undo(self):
        try:
            value = self.undo_stack.pop()
        except IndexError:
            print 'Nothing to undo'
            return False
        for row in self.board:
            if not row[value] == ' ':
                row[value] = ' '
                return value

    def segment_indexes(self):

        # Get indexes from rows, columns and diagonal lines and combine them to segments
        rows = [[(y, x) for x in range(self.width)] for y in range(self.height)]
        columns = [[(x, y) for x in range(self.height)] for y in range(self.width)]

        up = [[(x, y) for x in xrange(self.height) for y in xrange(self.width)
               if x + y == z] for z in xrange(3, 9)]
        down = [[(x, y) for x in xrange(self.height) for y in xrange(self.width)
                 if x - y == z] for z in xrange(-3, 3)]

        segments = rows + columns + up + down

        # Split segments to smaller, 4 length pieces
        # These are every possible chain of four in the game
        # Each element in returned list is a list of indexes (which are tuples)

        return [segments[x][i:i+4] for x in range(len(segments)) for i in range(len(segments[x])-3)]

    def is_legal_moves_left(self):
        return ' ' in [self.board[0][x] for x in xrange(self.width)]

    def __str__(self):
        numbers = [str(x) for x in xrange(1, self.width + 1)]
        print colored(' ' + ' '.join(numbers), 'cyan')

        s = ''
        for row in self.board:
            s += colored('|', 'red') + colored('|', 'red').join(row) + colored('|\n', 'red')

        return s
