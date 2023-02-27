from itertools import combinations_with_replacement
import math


def findAB(max_twist=4, max_rank=4):
    for rankB in range(2, max_rank+1):
        for B in combinations_with_replacement(range(1, max_twist+1), rankB):
            for C in combinations_with_replacement(range(1, max_twist+1), rankB-2):
                # check condition:
                # for all c_i ex b_j, b_k, b_l with j!=k!=l!=j such that b_j < c_i, b_k < c_i, b_l < c_i
                how_many_b_smaller_than_c = 0
                for c in C:
                    how_many_b_smaller_than_c = 0
                    for b in B:
                        if b<c:
                            how_many_b_smaller_than_c += 1
                        if how_many_b_smaller_than_c == 3:
                            break

                # check condition:
                # for all b_j ex c_i such that b_j<c_i
                c_big_enough_condition_satisfied = True
                for b in B:
                    is_this_b_okay = False
                    for c in C:
                        if c>b:
                            is_this_b_okay = True
                            break
                    if not is_this_b_okay:
                        c_big_enough_condition_satisfied = False
                        break
                Bsquare = sum([x**2 for x in B])
                Csquare = sum([x**2 for x in C])
                print(Bsquare-Csquare, sum(B)-sum(C), B, C, end='')
                if how_many_b_smaller_than_c < 3 or not c_big_enough_condition_satisfied:
                    print('x')
                else:
                    print('\n', end='')
                if how_many_b_smaller_than_c >= 3 and \
                        c_big_enough_condition_satisfied and \
                        Bsquare-Csquare == -1 and \
                        sum(B)-sum(C)==1:
                    input('Solution found')

def findAB_simple_criterion(max_twist=4, max_rank=4):
    for rankB in range(2, max_rank+1):
        for B in combinations_with_replacement(range(1, max_twist+1), rankB):
            for C in combinations_with_replacement(range(1, max_twist+1), rankB-2):
                # check condition:
                # for all c_i ex b_j, b_k, b_l with j!=k!=l!=j such that b_j < c_i, b_k < c_i, b_l < c_i
                how_many_b_smaller_than_c = 0
                for c in C:
                    how_many_b_smaller_than_c = 0
                    for b in B:
                        if b<c:
                            how_many_b_smaller_than_c += 1
                        if how_many_b_smaller_than_c == 3:
                            break

                # check condition:
                # for all b_j ex c_i such that b_j<c_i
                c_big_enough_condition_satisfied = True
                for b in B:
                    is_this_b_okay = False
                    for c in C:
                        if c>b:
                            is_this_b_okay = True
                            break
                    if not is_this_b_okay:
                        c_big_enough_condition_satisfied = False
                        break
                Bsquare = sum([x**2 for x in B])
                Csquare = sum([x**2 for x in C])
                print(Bsquare-Csquare, sum(B)-sum(C), B, C, end='')
                if how_many_b_smaller_than_c < 3 or not c_big_enough_condition_satisfied:
                    print('x')
                else:
                    print('\n', end='')
                if how_many_b_smaller_than_c >= 3 and \
                        c_big_enough_condition_satisfied and \
                        Bsquare-Csquare == -1 and \
                        sum(B)-sum(C)==1:
                    input('Solution found')


if __name__ == '__main__':
    findAB()
