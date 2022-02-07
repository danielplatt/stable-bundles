'''Implementation of
An Explicit Algorithm for Computing the Picard Number of Certain Algebraic Surfaces
Author(s): Tetsuji Shioda
https://www.jstor.org/stable/pdf/2374678.pdf?refreqid=excelsior%3Aa5ea099e65db9eae2ba9c2d655762b4c'''

import numpy as np
import itertools

from util.compositions import compositions
from log import get_logger
import logging

log = get_logger(__name__, with_logfile=True, level=logging.INFO)


def matrix_cofactor(matrix):
    return np.linalg.inv(matrix) * np.linalg.det(matrix)

def cofactor_test():
    A = np.array([[0, 0, 0, 4],
                  [0, 0, 1, 3],
                  [0, 1, 0, 3],
                  [1, 0, 3, 0]])
    print(np.linalg.det(A))
    print(np.matmul(A, matrix_cofactor(A)))

def get_delta(matrix):
    # print(matrix_cofactor(matrix))
    cof = np.rint(matrix_cofactor(matrix)).astype('int16')
    # print(cof)
    delta = np.gcd.reduce(cof.flatten())
    return delta

def get_d(matrix):
    d = abs(np.linalg.det(matrix))/get_delta(matrix)
    return int(np.round(d))

def get_B_matrix(matrix):
    d = get_d(matrix)
    B = np.rint(d*np.linalg.inv(matrix)).astype('int16')
    # print(B)
    # Bprime = np.rint(1/get_delta(matrix)*matrix_cofactor(matrix))
    # print(Bprime)
    # exit()
    return B

def get_iterator_of_A():
    prod_generator = itertools.product(compositions(4, 4),compositions(4, 4),
                                       compositions(4, 4),compositions(4, 4))
    return prod_generator


    # A = np.array([
    #     [4,0,0,0],
    #     [1,3,0,0],
    #     [0,1,3,0],
    #     [0,0,0,4]
    # ]) # should give 10
    #
    # A = np.array([
    #     [1,3,0,0],
    #     [0,1,3,0],
    #     [3,0,1,0],
    #     [0,0,0,4]
    # ], dtype='int8') # should give 20
    # A = np.array([
    #     [4,0,0,0],
    #     [0,4,0,0],
    #     [0,0,4,0],
    #     [0,0,0,4]
    # ], dtype='int8')
    # A = np.array([[0, 0, 0, 4],
    #  [0, 0, 1, 3],
    #  [0, 1, 0, 3],
    #  [1, 0, 3, 0]]) # singular
    A = np.array([[0, 0, 0, 4], [0, 0, 3, 1], [0, 3, 1, 0], [3, 1, 0, 0]])
    return [A]

def check_valid_A(matrix) -> bool:
    if np.rint(np.linalg.det(matrix)) == 0:
        return False
    # check if each column contains zero
    if not np.array_equal(matrix.min(axis=0), [0,0,0,0]):
        return False

    # smoothness check: check if each column contains a 3 or a 4
    # otherwise, if first column contains no 3 and no 4, then
    # [1:0:0:0] is singular point
    if np.all(np.greater_equal(matrix.max(axis=0), [3,3,3,3])):
        return True
    else:
        return False

def get_M_d_module(matrix) -> set:
    M = set()
    delta = get_delta(matrix)
    d = get_d(matrix)
    # print(matrix)
    # print('delta=%s, d=%s' % (delta, d))
    for tuple in itertools.product(range(d), repeat=3):
        M.add((tuple[0], tuple[1], tuple[2], (-tuple[0]-tuple[1]-tuple[2])%d))
    return M

def get_L_A_module(matrix) -> set:
    L = set()
    B = get_B_matrix(matrix)
    # print(B)
    # print(1/get_delta(matrix)*matrix_cofactor(matrix))
    d = get_d(matrix)
    for tup in get_M_d_module(matrix):
        new_el = list(np.mod(np.matmul(np.array(tup), B), d))
        # print(np.array(tup), new_el, np.matmul(np.array(tup), B))
        L.add(tuple(new_el))
    return L

def get_A_squared_d(matrix):
    A = set()
    log.debug('d=%s, delta=%s' % (get_d(matrix), get_delta(matrix)))
    M = get_M_d_module(matrix)
    log.debug('len(M)=%s' % len(M))
    for tup in M:
        if tup[0] != 0 \
                and tup[1] != 0 \
                and tup[2] != 0 \
                and tup[3] != 0:
            A.add(tup)
    log.debug('len(A)=%s' % len(A))
    return A

def get_B_squared_d(matrix):
    B = set()
    d = get_d(matrix)
    A = get_A_squared_d(matrix)
    for (k,tup) in enumerate(A):
        if k%10000 == 0:
            log.debug('Computing B^2_d. Element %s/%s.' % (k, len(A)))
        add_tup = True
        for t in range(d):
            if np.gcd(t,d) == 1:
                vec = [t*a/d for a in tup]
                vecNew = [entry-np.floor(entry) for entry in vec]
                if int(np.rint(sum(vecNew)))!=2:
                    add_tup = False
                    break
        if add_tup:
            B.add(tup)
    log.debug('len(B)=%s' % len(B))
    return B

def L_example_calc():
    alpha = np.array([1,-4,12,-9])
    for k in range(1000):
        print(np.mod(k*alpha, 36), np.mod(k*alpha, 36).max())
        if np.mod((k+1)*alpha, 36).max() == 0:
            print((k+1))
            exit()

def get_picard(matrix):
    A = get_A_squared_d(matrix)
    B = get_B_squared_d(matrix)
    L = get_L_A_module(matrix)

    I = A - B
    # print(get_M_d_module(matrix))
    # print(L)
    # print(get_d(matrix))
    # print(len(A),len(B),len(L),len(I))
    lam = len(I.intersection(L))
    rho = 22 - lam
    return rho


if __name__ == '__main__':
    skip_to = 4161
    gen = get_iterator_of_A()
    inv_counter = 0
    for (k, A) in enumerate(gen):
        if k<skip_to:
            continue
        A = np.array(A)
        if check_valid_A(A):
            log.info('ID: %s, rho=%s, A=%s' % (k, get_picard(A), list(A)))
        # else:
        #     if inv_counter % 1000 ==0:
        #         log.info('Invalid number %s: %s' % (inv_counter, list(A)))
        #     inv_counter += 1

