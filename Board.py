#!/usr/bin/env python
# -*- coding: utf-8 -*-
from termcolor import colored   # mahollisesti poista et toimii kaikilla


class Board:
    """Game board for Connect 4"""
    def __init__(self, width=7, height=6):
        self.width = width
        self.height = height
        self.board = self.build_board(width, height)
        self.game_over = False

    def build_board(self, width, height):
        return [[' ' for x in range(width)] for x in range(height)]

    def print_board(self):
        print ''
        numbers = [str(x) for x in range(1, self.width + 1)]
        print colored(' ' + ' '.join(numbers), 'cyan')

        for row in self.board:
            print colored('|', 'red') + colored('|', 'red').join(row) + colored('|', 'red')

    def place_piece(self, move, curr_player, opponent):
        for row in reversed(self.board):
            if row[move-1] == ' ':
                row[move-1] = curr_player.sign
                self.is_gameover(curr_player, opponent)
                return True

        print 'Not allowed'
        return False

    def is_gameover(self, curr_player, opponent):
        curr_sign = curr_player.sign
        opp_sign = opponent.sign

        # check rows
        for row in self.board:
            row = ''.join(row)
            if 4*curr_sign in row or 4*opp_sign in row:
                if curr_player.is_ai:
                    # Comp won
                    print 'You lost!'
                else:
                    # Player has won
                    print 'You won!'

                self.game_over = True

        # check columns
        for column in range(self.height):
            s = ''
            for row in self.board:
                s += row[column]

            if 4*curr_sign in s or 4*opp_sign in s:
                if curr_player.is_ai:
                    # Comp won
                    print 'You lost!'
                else:
                    # Player has won
                    print 'You won!'

                self.game_over = True

        # check diagonals
        up = [''.join([self.board[x][y] for x in range(self.height) for y in range(self.width)
              if x+y == z]) for z in range(3, 9)]

        down = [''.join([self.board[x][y] for x in range(self.height) for y in range(self.width)
                if x-y == z]) for z in range(-3, 3)]

        up = [x.lstrip() for x in up]   # remove preceding spaces
        down = [x.lstrip() for x in down]   # remove preceding spaces

        if 4*curr_sign in up or 4*curr_sign in down or 4*opp_sign in up or 4*opp_sign in down:
            if curr_player.is_ai:
                # Comp won
                print 'You lost!'
            else:
                # Player has won
                print 'You won!'

            self.game_over = True