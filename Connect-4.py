#!/usr/bin/env python
# -*- coding: utf-8 -*-
from random import randint
from Board import Board


def main():
    board = Board()
    play(board)


def play(board):
    print "Let's play four in a row\nTo place a move, type a number [1-7]"

    while not board.game_over:
        board.print_board()
        p_move = int(raw_input())
        board.place_piece(p_move, 'X')

        if board.game_over:
            print 'Game over'
            game_over()

        c_move = comp_move(board)
        board.place_piece(c_move, 'O')

    print 'Game over'
    game_over()


def comp_move(board):
    return randint(1, 7)


def game_over():
    ans = raw_input('Do you want to play again? y/n\n')
    if ans.lower() == 'y':
        main()
    else:
        raise SystemExit(0)


main()
