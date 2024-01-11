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
    Returns the first Chern class of the bundle K fitting into the
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
    c2B = second_chern_of_free_bundle(B)
    c2C = second_chern_of_free_bundle(C)
    return int(c2B-c1B*c1C+c1C**2-c2C)

def rank_of_cohom_monad(A: list, B: list, C: list) -> int:
    dim_ker_b = len(B)-len(C)
    return dim_ker_b-len(A)

def first_chern_of_cohom_monad(A: list, B: list, C: list) -> int:
    return first_chern_of_free_bundle(B)-first_chern_of_free_bundle(C)-first_chern_of_free_bundle(A)

def second_chern_of_cohom_monad(A: list, B: list, C: list) -> int:
    c1A = first_chern_of_free_bundle(A)
    c1B = first_chern_of_free_bundle(B)
    c1C = first_chern_of_free_bundle(C)
    c2A = second_chern_of_free_bundle(A)
    c2B = second_chern_of_free_bundle(B)
    c2C = second_chern_of_free_bundle(C)
    return (c1C**2-c2C)+(c1A**2-c2A)+(c2B)+(c1A*c1C-c1A*c1B-c1B*c1C)

def find_kernel_monads():
    MAX_RANK_B = 3
    MIN_TWIST = -5
    MAX_TWIST = 5
    MIN_C2 = -999
    MAX_C2 = 999

    for rB in range(2, MAX_RANK_B+1):
        rC = rB - 2
        for B in combinations_with_replacement(range(MIN_TWIST, MAX_TWIST+1), rB):
            for C in combinations_with_replacement(range(max(B), MAX_TWIST+1), rC):
                # previously this said (range(max(B), MAX_TWIST+1). TO be sure that bundle map exists

                # good chern class?
                c2 = second_chern_of_kernel_monad(B, C)
                c1 = first_chern_of_kernel_monad(B, C)
                if 2*(-4*c2+c1**2) == -6 and c2 >= MIN_C2 and c2 <= MAX_C2:
                    # that means 0-dim moduli space, cf. p.345
                    k=-math.floor(c1/2) # the normalisation number for the DUAL bundle
                    if -k-min(B)<0: # this is for the Hoppe criterion check
                        print('! ', end='')
                    print('c1=%s, c2=%s. B=%s, C=%s, k=%s' % (c1, c2, B, C, k))
                    # check if Hoppe criterion can be applied to dual bundle
                    # kdual = int((c1+1)/2)
                    # if k + min(B) > 0

def find_cokernel_monads():
    MAX_RANK_B = 4 # hoppe crit only checked correctly if =3
    MIN_TWIST = -5
    MAX_TWIST = 5
    MIN_C2 = -999
    MAX_C2 = 999

    for rB in range(2, MAX_RANK_B+1):
        rA = rB - 2
        for B in combinations_with_replacement(range(MIN_TWIST, MAX_TWIST+1), rB):
            for A in combinations_with_replacement(range(MIN_TWIST, MAX_TWIST+1), rA):
                # good chern class?
                c2 = second_chern_of_cokernel_monad(A, B)
                c1 = first_chern_of_cokernel_monad(A, B)
                if 2*(-4*c2+c1**2) == -6 and c2 >= MIN_C2 and c2 <= MAX_C2:
                    # that means 0-dim moduli space, cf. p.345
                    k=int((-c1+1)/2)
                    if k+max(B)<0: # this is for the Hoppe criterion check
                        print('k=%s' % (k,))
                        print('! c1=%s, c2=%s. A=%s, B=%s' % (c1, c2, A, B))

def find_cohom_monads():
    offset_tensor = -4
    A=[-3+offset_tensor]
    for B_partial in combinations_with_replacement(range(-2+offset_tensor,15+offset_tensor), 3):
        B = list(B_partial) + [0+offset_tensor]
        C=[max(B)+1]
        if -first_chern_of_cohom_monad(A,B,C)**2 +4*second_chern_of_cohom_monad(A,B,C) == 3:
            print('!', end='')
            print(first_chern_of_cohom_monad(A,B,C), second_chern_of_cohom_monad(A,B,C), A, B, C)

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

def find_stable_cohom_mondas():
    MIN_TWIST = -30
    MAX_TWIST = 30
    finds = []
    for a in range(MIN_TWIST, MAX_TWIST):
        A = [a]
        for B_part1 in range(a+3, MAX_TWIST):
            for B_part2 in combinations_with_replacement(range(a+1, MAX_TWIST), 3):
                B = [B_part1] + list(B_part2)
                for c in range(max(B)+1, MAX_TWIST):
                    C = [c]
                    # rigidity check
                    if -first_chern_of_cohom_monad(A, B, C) ** 2 + 4 * second_chern_of_cohom_monad(A, B, C) == 3:
                        if first_chern_of_cohom_monad(A, B, C) == -1:
                            # check if map of complexes exists
                            if check_weight_difference_allows_complex_maps(A, B, C):
                                print('!', end='')
                                finds += [A, B, C]
                            # stability check
                            if max(B)<0:
                                print('!', end='')
                            print(first_chern_of_cohom_monad(A,B,C), second_chern_of_cohom_monad(A,B,C), A, B, C, end='')
                            print(finds)


if __name__ == '__main__':
    print(first_chern_of_free_bundle([(1,2), (-1,0)]))
    print(second_chern_of_free_bundle([(1,2), (-1,0)]))
    # find_stable_cohom_mondas()
