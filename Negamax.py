#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
""" 
This heuristic algorithm is based on negamax, which is a variant of a minimax algorithm.
Negamax can be used due to zero-sum property of Connect-4. Heuristic algorithm is 
needed, because Connect Four has around 4*10^12 (4 trillion) different possible games.
"""


class Negamax:

    def __init__(self, board, max_depth=4):
        self.listed_indexes = board.segment_indexes()
        self.weights = [1, 16, 256, 9999999]
        self.max_depth = max_depth

    def negamax(self, board, curr_sign, opponent_sign, depth=0):
        if depth == self.max_depth:
            if not self.check_if_evaluated(board):
                score = self.evaluate(board.board, curr_sign, opponent_sign)
                self.evaluated[hash(board)] = score
                return None, score
            else:
                return None, self.evaluated[hash(board)]

        best_score = float('-inf')
        best_move = None

        for x in xrange(1, 8):
            move = x
            move_allowed = board.place_piece(move, curr_sign)
            if not move_allowed:
                continue
            best_submove, best_subscore = self.negamax(board, opponent_sign, curr_sign, depth + 1)
            best_subscore *= -1
            board.undo()
            if best_subscore > best_score:
                best_score = best_subscore
                best_move = move

        return best_move, best_score

    def evaluate(self, board, curr_sign, opponent_sign):
        """Counts and weighs longest connected checker chains which can lead to win"""

        curr_score = 0
        opp_score = 0

        for indexes in self.listed_indexes:
            # indexes contains four board indexes as tuples

            curr_count = 0
            opp_count = 0

            for index in indexes:
                v = board[index[0]][index[1]]
                if v == curr_sign:
                    curr_count += 1
                elif v == opponent_sign:
                    opp_count += 1

            if curr_count > 0 and opp_count > 0:
                continue
            elif curr_count > 0:
                curr_score += curr_count * self.weights[curr_count-1]
            elif opp_count > 0:
                opp_score += opp_count * self.weights[opp_count-1]

        difference = curr_score - opp_score

        return difference
