from itertools import combinations_with_replacement
import math


def first_chern_of_free_bundle(bundle: list) -> int:
    """
    Computes the first Chern class of a bundle of the form
    O(m1,n1)+...+O(mk,nk).

    :param bundle: A list of 2-tuples encoding the bundle. For
    example, [(1, 2), (0, -1)] encodes the rank 2 vector bundle
    O(1,2)+O(0,-1).
    :return: Returns the first Chern class as a 2-tuple, where we
    identified the second cohomology of P^1xP^1 with 2-tuples
    by choosing the two generators which are pulled back from each
    of the two P^1 factors.
    """
    firstchern = [0,0]
    for factor in bundle:
        firstchern[0] += factor[0]
        firstchern[1] += factor[1]
    return tuple(firstchern)

def second_chern_of_free_bundle(bundle: list) -> int:
    """
    Computes the second Chern class of a bundle of the form
    O(m1,n1)+...+O(mk,nk).

    :param bundle: A list of 2-tuples encoding the bundle. For
    example, [(1, 2), (0, -1)] encodes the rank 2 vector bundle
    O(1,2)+O(0,-1).
    :return: Returns the first Chern class as a single integer, where we
    identified the fourth cohomology of P^1xP^1 with the integers.
    """
    chern = 0
    for k in range(len(bundle)):
        chern += sum([bundle[k][0]*i[1]+bundle[k][1]*i[0] for i in bundle[k+1:]])
    return chern

def rank_of_kernel_monad(B: list, C: list) -> int:
    return len(B)-len(C)

def first_chern_of_kernel_monad(B: list, C: list) -> int:
    """
    Returns the first Chern class of the bundle K fitting into the
    short exact sequence
    0->K->B->C->0.

    :param B: A list of 2-tuples encoding the bundle. For
    example, [(1, 2), (0, -1)] encodes the rank 2 vector bundle
    O(1,2)+O(0,-1).
    :param C: Same format as B.
    :return: Returns the first Chern class as a 2-tuple, where we
    identified the second cohomology of P^1xP^1 with 2-tuples
    by choosing the two generators which are pulled back from each
    of the two P^1 factors.
    """
    chernresult = [0, 0]
    for factor in B:
        chernresult[0] += factor[0]
        chernresult[1] += factor[1]
    for factor in C:
        chernresult[0] -= factor[0]
        chernresult[1] -= factor[1]
    return chernresult

def second_chern_of_kernel_monad(B: list, C: list) -> int:
    """
    Returns the second Chern class of the bundle K fitting into the
    short exact sequence
    0->K->B->C->0.

    :param B: A list of 2-tuples encoding the bundle. For
    example, [(1, 2), (0, -1)] encodes the rank 2 vector bundle
    O(1,2)+O(0,-1).
    :param C: Same format as B.
    :return: Returns the second Chern class as an integer, where
    we identified the fourth cohomology of P^1xP^1 with the integers.
    """
    c1B = first_chern_of_free_bundle(B)
    c1C = first_chern_of_free_bundle(C)
    c1B_times_c1C = c1B[0]*c1C[1]+c1B[1]*c1C[0]
    c1C_squared = c1C[0]*c1C[1]+c1C[1]*c1C[0]
    c2B = second_chern_of_free_bundle(B)
    c2C = second_chern_of_free_bundle(C)
    return int(c2B-c1B_times_c1C+c1C_squared-c2C)

def find_kernel_monads(monad_rank: int):
    MAX_RANK_B = 4
    MIN_TWIST = -2
    MAX_TWIST = 2
    MIN_C2 = -999
    MAX_C2 = 999


    for rB in range(monad_rank+1, MAX_RANK_B+1):
        rC = rB - monad_rank
        for b1 in combinations_with_replacement(range(MIN_TWIST, MAX_TWIST+1), rB):
            for b2 in combinations_with_replacement(range(MIN_TWIST, MAX_TWIST+1), rB):
                for c1 in combinations_with_replacement(range(MIN_TWIST, MAX_TWIST+1), rC):
                    for c2 in combinations_with_replacement(range(MIN_TWIST, MAX_TWIST + 1), rC):
                        # Can a bundle map exist?
                        if max(b1) < max(c1) and max(b2) < max(c2):
                            # is this a rigid bundle?
                            B = list(zip(b1, b2))
                            C = list(zip(c1, c2))
                            c2 = second_chern_of_kernel_monad(B, C)
                            c1 = first_chern_of_kernel_monad(B, C)
                            c1_squared = c1[0] * c1[1] + c1[1] * c1[0]
                            virtual_dimension = 2 * monad_rank * (2 * c2) - (monad_rank - 1) * 2 * (c1_squared) - 2 * (monad_rank ** 2 - 1)
                            if virtual_dimension == 0:
                                print('! ', end='')
                                print('c1=%s, c2=%s. B=%s, C=%s' % (c1, c2, B, C))
                            # if virtual_dimension == 0:
                            #     input()

def check_weight_difference_allows_complex_maps(A, B, C):
    for num_b, b in enumerate(B):
        diff_ab = b-A[0]
        for num_b_tilde, b_tilde in enumerate(B):
            diff_b_tilde_c = C[0]-b_tilde
            if num_b != num_b_tilde and diff_ab == diff_b_tilde_c and diff_ab%3 == 0:
                print('w/z indices: %s and %s' % (num_b, num_b_tilde))
                B_leftover = [b for k, b in enumerate(B) if k!=num_b and k!=num_b_tilde]
                print(B_leftover)
                print('x/z index search: %s ~ %s' % (B_leftover[0]-A[0], C[0]-B_leftover[1]))
                if B_leftover[0]-A[0] == C[0]-B_leftover[1]:
                    return True


if __name__ == '__main__':
    print(first_chern_of_free_bundle([(1,2), (-1,0)]))
    print(second_chern_of_free_bundle([(1,2), (-1,0)]))
    B = [(0,0), (0,0), (0,0), (0,0)]
    C = [(1,1)]
    print(first_chern_of_kernel_monad(B, C))
    print(second_chern_of_kernel_monad(B, C))

    find_kernel_monads(3)
    # find_stable_cohom_mondas()
