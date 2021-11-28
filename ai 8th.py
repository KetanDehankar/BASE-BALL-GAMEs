# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 23:59:45 2021

@author: Keytan
"""

def solution():
   # letters = ('b','a','s','e','l','g','m')
    all_solution = list()
    for b in range(9, -1, -1):
        for a in range(9, -1, -1):
            for s in range(9, -1, -1):
                for e in range(9, -1, -1):
                    for l in range(9, -1, -1):
                        for g in range(9, -1, -1):
                            for m in range(9, -1, -1):
                                    if len(set([b, a, s, e, l, g, m] ) ) == 7:
                                        base = 1000 * b + 100 * a + 10 * s + e
                                        ball = 1000 * b + 100 * a + 10 * l + l
                                        games = 10000 * g + 1000 * a + 100 * m + 10 * e + s
                                        if base + ball == games:
                                            all_solution.append((base, ball, games))
                                            return all_solution
print(solution())
                                        