#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Board import Board
from Players import HumanPlayer, AIPlayer


def play():
    board = Board()
    human = HumanPlayer()
    ai = AIPlayer('Y')

    print "Let's play connect four!\nTo place a move, type a number [1-7]"

    current_player = human
    other_player = ai

    while not board.game_over:
        board.print_board()

        move_allowed = False
        while not move_allowed:
            move_allowed = board.place_piece(current_player.get_move(board),
                                             current_player, other_player)

        if current_player is human:
            current_player = ai
            other_player = human
        else:
            current_player = human
            other_player = ai

    print 'Game over'
    ans = raw_input('Do you want to play again? y/n\n')

    if ans.lower() == 'y':
        play()
    else:
        raise SystemExit(0)

play()
