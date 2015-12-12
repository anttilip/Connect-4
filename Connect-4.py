#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Board import Board
from Players import HumanPlayer, AIPlayer


def play():
    board = Board()
    human = HumanPlayer()
    ai = AIPlayer()

    print "Let's play connect four!\nTo place a move, type a number [1-7]"

    current_player = human

    while not board.game_over:
        board.print_board()

        move_allowed = False
        while not move_allowed:
            move_allowed = board.place_piece(current_player.get_move(),
                                             current_player.sign)

        # current_player = ai if current_player is human else human     # maybe confusing?
        if current_player is human:
            current_player = ai
        else:
            current_player = human

    print 'Game over'
    ans = raw_input('Do you want to play again? y/n\n')

    if ans.lower() == 'y':
        play()
    else:
        raise SystemExit(0)

play()
