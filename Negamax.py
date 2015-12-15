#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" 
This heuristic algorithm is based on negamax, which is a variant of a minimax algorithm.
Negamax can be used due to zero-sum property of Connect-4. Heuristic algorithm is 
needed, because Connect Four has around 5*10^12 different possible games.
"""


class Negamax:

    def pef(self, board):
        """Position evaluation function counts and weighs longest connected 
        checker chains"""

        p1_sign = 'X'
        p2_sign = 'O'

        segments = board.segments()

        weights = [1, 4, 8, float('inf')]

        p1_score = 0
        for s in segments:
            for x in xrange(4, 0, -1):
                if x * p1_sign in s:
                    p1_score += weights[x-1]
                    break

        p2_score = 0
        for s in segments:
            for x in xrange(4, 0, -1):
                if x * p2_sign in s:
                    p2_score += weights[x-1]
                    break

        difference = p1_score - p2_score

        return difference, p1_score, p2_score





