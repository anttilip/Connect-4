#!/usr/bin/env python
# -*- coding: utf-8 -*-
from random import randint


class HumanPlayer():
    sign = 'X'

    def get_move(self):
        return int(raw_input())


class AIPlayer():
    sign = 'O'

    def get_move(self):
        return randint(1, 7)
