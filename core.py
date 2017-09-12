from random import choice
from termcolor import cprint
import os


class Futbol:
    """ A soccer player shoot a pk and either scores or misses."""

    def __init__(self, name, team):
        """(Futbol, str, str) -> NoneType"""
        self.score = 0
        self.team = team
        self.name = name
        self.attempts = 5

    def __str__(self):
        return 'Name: {0} | Team: {1} | Score: {2} | Remaining Shots: {3}'.format(
            self.name, self.team, self.score, self.attempts)

    def __repr__(self):

        return 'Futbol({0}, Score: {1}, Miss: {2}, Attempts: {3}'.format(
            self.name, self.score, self.miss, self.attempts)

    def shoot(self):
        self.attempts -= 1
        maybe = choice([True, False])
        if maybe == True:
            self.score += 1
            os.system('clear')
            cprint(r'''
                                     
                        	             	                                                88  
                        	 	                                                        88  
,adPPYb,d8   ,adPPYba,   ,adPPYba,   ,adPPYba,    ,adPPYba,   ,adPPYba,   ,adPPYba,  ,adPPYYba, 88  
a8"    `Y88 a8"     "8a a8"     "8a a8"     "8a  a8"     "8a a8"     "8a a8"     "8a ""     `Y8 88  
8b       88 8b       d8 8b       d8 8b       d8	 8b       d8 8b       d8 8b       d8 ,adPPPPP88 88  
"8a,   ,d88 "8a,   ,a8" "8a,   ,a8" "8a,   ,a8"	 "8a,   ,a8" "8a,   ,a8" "8a,   ,a8" 88,    ,88 88  
 `"YbbdP"Y8  `"YbbdP"'   `"YbbdP"'   `"YbbdP"'    `"YbbdP"'   `"YbbdP"'   `"YbbdP"'  `"8bbdP"Y8 88  
 aa,    ,88                            
  "Y8bbdP"         ''', 'blue')

            os.system('espeak "GOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOL!"')

        elif maybe == False:
            os.system('clear')

            cprint(
                r'''                                                     88  
                                                     88  
                                                     88  
,adPPYba, ,adPPYYba, 8b       d8  ,adPPYba,  ,adPPYb,88  
I8[    "" ""     `Y8 `8b     d8' a8P_____88 a8"    `Y88  
 `"Y8ba,  ,adPPPPP88  `8b   d8'  8PP""""""" 8b       88  
aa    ]8I 88,    ,88   `8b,d8'   "8b,   ,aa "8a,   ,d88  
`"YbbdP"' `"8bbdP"Y8     "8"      `"Ybbd8"'  `"8bbdP"Y8  
                                                         ''', 'blue')
            os.system('espeak "What a save!"')


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def keep_game_going(self):
        attempts = self.p1.attempts
        diff = abs(self.p1.score - self.p2.score)
        if diff > attempts:
            return False
        if attempts == 0:
            if diff > 0:
                return False
            else:

                self.p1.attempts = 5
                self.p2.attempts = 5
                return True
        return True

    def winner(self):
        w, l = self.p2, self.p1
        if self.p1.score > self.p2.score:
            w, l = self.p1, self.p2
        os.system(
            'espeak "{}     IS THE WINNER!     {}     loses...     \nFinal Score {}   to   {}"'.
            format(w.name, l.name, w.score, l.score))
        return '{} IS THE WINNER! {} loses...\nFinal Score {} to {}'.format(
            w.name, l.name, w.score, l.score)
