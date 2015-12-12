#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Board:
    """Game board for Connect 4"""
    def __init__(self, n=7, m=6):
        self.n = n
        self.m = m
        self.board = self.build_board(n, m)
        self.game_over = False

    def build_board(self, n, m):
        return [[' ' for x in range(n)] for x in range(m)]

    def print_board(self):
        print ''
        numbers = [str(x) for x in range(1, self.n + 1)]
        print ' ' + ' '.join(numbers)

        for row in self.board:
            print '|' + '|'.join(row) + '|'

    def place_piece(self, move, player):
        for row in reversed(self.board):
            if row[move-1] == ' ':
                row[move-1] = player
                self.is_gameover()
                return True

        print 'Not allowed'
        return False

    def is_gameover(self):
        n = len(self.board[0])
        m = len(self.board)

        # check rows
        for row in self.board:
            if 4*'X' in ''.join(row):
                # Player has won
                print 'You won!'
                self.game_over = True
            elif 4*'O' in ''.join(row):
                # Comp has won
                print 'You lost!'
                self.game_over = True

        # check columns
        for column in range(m):
            s = ''
            for row in self.board:
                s += row[column]

            if 4*'X' in s:
                # Player won
                print 'You won!'
                self.game_over = True

            elif 4*'O' in s:
                # Comp won
                print 'You lost!'
                self.game_over = True

        # check diagonals
        up = [''.join([self.board[x][y] for x in range(m) for y in range(n)
              if x+y == z]) for z in range(3, 9)]

        down = [''.join([self.board[x][y] for x in range(m) for y in range(n)
                if x-y == z]) for z in range(-3, 3)]

        up = [x.lstrip() for x in up]   # remove preceding spaces
        down = [x.lstrip() for x in down]   # remove preceding spaces

        if 4*'X' in up or 4*'X' in down:
            # Player won
            print 'You won!'
            self.game_over = True

        elif 4*'O' in up or 4*'O' in down:
            # Comp won
            print 'You lost!'
            self.game_over = True
