from itertools import combinations_with_replacement
import math
from tqdm import tqdm


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

def first_segre_of_free_bundle(bundle: list) -> int:
    firstchern = first_chern_of_free_bundle(bundle)
    return (-firstchern[0], -firstchern[1])

def second_segre_of_free_bundle(bundle: list) -> int:
    # s2=s1^2-c2
    firstsegre = first_segre_of_free_bundle(bundle)
    secondchern = second_chern_of_free_bundle(bundle)
    return 2*firstsegre[0]*firstsegre[1]-secondchern

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

def first_chern_of_cohomology_monad(A: list, B:list, C:list) -> int:
    chernresult = []


def is_monad_product_of_existing_monad(monad: list, found_monads: list):
    '''Tests if the given monad can be obtained from a monad in
    found_monads by tensoring with (0,1) or (1,0).'''
    for comparing_monad in found_monads:
        B_compare_tensor_one_zero = [(bun[0] + 1, bun[1]) for bun in comparing_monad[0]]
        C_compare_tensor_one_zero = [(bun[0] + 1, bun[1]) for bun in comparing_monad[1]]
        B_compare_tensor_zero_one = [(bun[0], bun[1] + 1) for bun in comparing_monad[0]]
        C_compare_tensor_zero_one = [(bun[0], bun[1] + 1) for bun in comparing_monad[1]]
        if B_compare_tensor_one_zero == monad[0] and C_compare_tensor_one_zero == monad[1]:
            return True
        elif B_compare_tensor_zero_one == monad[0] and C_compare_tensor_zero_one == monad[1]:
            return True

def is_monad_sum_of_lower_rank_B_monad(monad: list, lower_rank_B_found_monads: list):
    '''Tests if monad can be obtained from lower_rank_B_found_monads
    by adding a line bundle'''
    for bun in monad[1]:
        try:
            index_in_B = monad[0].index(bun)
        except ValueError as e:
            continue
        reduced_B = monad[0][:]
        del reduced_B[index_in_B]
        index_in_C = monad[1].index(bun)
        reduced_C = monad[1][:]
        del reduced_C[index_in_C]
        if (reduced_B, reduced_C) in lower_rank_B_found_monads:
            return True

def find_kernel_monads(monad_rank: int, MAX_RANK_B = 6, MIN_TWIST = 0, MAX_TWIST = 1):

    one_rank_lower_B_found_monad_list = []
    for rB in range(monad_rank+1, MAX_RANK_B+1):
        rC = rB - monad_rank
        found_monad_list = []
        for b1 in list(combinations_with_replacement(range(MIN_TWIST, MAX_TWIST+1), rB)):
            for b2 in combinations_with_replacement(range(MIN_TWIST, MAX_TWIST+1), rB):
                for c1 in combinations_with_replacement(range(MIN_TWIST, MAX_TWIST+1), rC):
                    for c2 in combinations_with_replacement(range(MIN_TWIST, MAX_TWIST + 1), rC):
                        # Can a bundle map exist?
                        if max(b1) < max(c1) and max(b2) < max(c2) and min(b1) < min(c1) and min(b2) < min(c2):
                            # is this a rigid bundle?
                            B = list(zip(b1, b2))
                            C = list(zip(c1, c2))
                            c2 = second_chern_of_kernel_monad(B, C)
                            c1 = first_chern_of_kernel_monad(B, C)
                            c1_squared = c1[0] * c1[1] + c1[1] * c1[0]
                            virtual_dimension = 2 * monad_rank * (2 * c2) - (monad_rank - 1) * 2 * (c1_squared) - 2 * (monad_rank ** 2 - 1)
                            if virtual_dimension == 0:
                                found_monad_list += [(B,C)]
                                print('! ', end='')
                                print('c1=%s, c2=%s. B=%s, C=%s' % (c1, c2, B, C), end='')
                                if is_monad_product_of_existing_monad([B, C], found_monad_list):
                                    print(' (duplicate: product)')
                                elif is_monad_sum_of_lower_rank_B_monad([B, C], one_rank_lower_B_found_monad_list):
                                    print(' (duplicate: from lower rank)')
                                else:
                                    print(' (new)')
        one_rank_lower_B_found_monad_list = found_monad_list

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

def find_cohomology_monads(monad_rank: int, MAX_RANK_A = 6, MIN_RANK_B = 6, MAX_RANK_B = 6, MIN_TWIST = 0, MAX_TWIST = 1):
    found_monad_list = []

    # A = [(0,0)]
    # B = [(1,1),(1,1),(1,1),(1,1)]
    # C = [(2,2)]
    # exit()

    for rA in range(1,MAX_RANK_A+1):
        smallest_vir_dim = 1000
        for rB in range(MIN_RANK_B,MAX_RANK_B + 1):
            rC = rB - rA - monad_rank
            if rC < 1:
                continue
            for a1 in list(combinations_with_replacement(range(MIN_TWIST, MAX_TWIST + 1), rA)):
                for a2 in combinations_with_replacement(range(MIN_TWIST, MAX_TWIST + 1), rA):
                    for b1 in list(combinations_with_replacement(range(MIN_TWIST, MAX_TWIST + 1), rB)):
                        for b2 in combinations_with_replacement(range(MIN_TWIST, MAX_TWIST + 1), rB):
                            for c1 in combinations_with_replacement(range(MIN_TWIST, MAX_TWIST + 1), rC):
                                for c2 in combinations_with_replacement(range(MIN_TWIST, MAX_TWIST + 1), rC):
                                    # Can bundle maps exist?
                                    # print(f'A={(a1,a2)}, B={(b1,b2)}, C={(c1,c2)}', end='')
                                    if max(b1) < max(c1) and max(b2) < max(c2) and min(b1) < min(c1) and min(b2) < min(c2) and max(a1) < max(b1) and max(a2) < max(b2) and min(a1) < min(b1) and min(a2) < min(b2):
                                        # is this a rigid bundle?
                                        A = list(zip(a1, a2))
                                        B = list(zip(b1, b2))
                                        C = list(zip(c1, c2))

                                        c1B = first_chern_of_free_bundle(B)
                                        c2B = second_chern_of_free_bundle(B)
                                        s1A = first_segre_of_free_bundle(A)
                                        s2A = second_segre_of_free_bundle(A)
                                        s1C = first_segre_of_free_bundle(C)
                                        s2C = second_segre_of_free_bundle(C)

                                        c1E = (c1B[0] + s1A[0] + s1C[0], c1B[1] + s1A[1] + s1C[1])

                                        s1A_times_c1B = s1A[0] * c1B[1] + s1A[1] * c1B[0]
                                        s1A_times_s1C = s1A[0] * s1C[1] + s1A[1] * s1C[0]
                                        c1B_times_s1C = c1B[0] * s1C[1] + c1B[1] * s1C[0]
                                        c2E = c2B + s2A + s2C + s1A_times_c1B + s1A_times_s1C + c1B_times_s1C

                                        # print(f'c(B)s(A)s(C): [1,{c1B},{c2B}]*[1,{s1A},{s2A}]*[1,{s1C},{s2C}]')
                                        # print(c1E, c2E)

                                        vir_dim = 2 * monad_rank * (2 * c2E) - (monad_rank - 1) * 2 * (
                                                    c1E[0] * c1E[1] + c1E[1] * c1E[0]) - 2 * (monad_rank ** 2 - 1)

                                        print(f'c1={c1E}, c2={c2E}. A={(a1,a2)}, B={(b1,b2)}, C={(c1,c2)}, vir_dim={vir_dim}', end='\n')
                                        smallest_vir_dim = min(smallest_vir_dim, vir_dim)
                                        if vir_dim == 0:
                                            found_monad_list += [(A,B,C)]
                                            print('! ', end='')
                                            print(f'c1={c1E}, c2={c2E}. A={(a1,a2)}, B={(b1,b2)}, C={(c1,c2)}', end='')
                                            # if is_monad_product_of_existing_monad([B, C], found_monad_list):
                                            #     print(' (duplicate: product)')
                                            # elif is_monad_sum_of_lower_rank_B_monad([B, C], one_rank_lower_B_found_monad_list):
                                            #     print(' (duplicate: from lower rank)')
                                            # else:
                                            #     print(' (new)')
                                            print('')
                                            input('')
    print(smallest_vir_dim)






if __name__ == '__main__':
    B = [(0,0), (0,0), (0,0), (0,0)]
    C = [(1,1)]
    print(f'B={B}, C={C}')
    print(f'1st Chern class of kernel monad K->B->C: {first_chern_of_kernel_monad(B, C)}')
    print(f'2nd Chern class of kernel monad K->B->C: {second_chern_of_kernel_monad(B, C)}')

    # find_kernel_monads(3, MAX_RANK_B = 5, MIN_TWIST = 0, MAX_TWIST = 3)
    find_cohomology_monads(3, MAX_RANK_A = 2, MIN_RANK_B = 6, MAX_RANK_B = 6, MIN_TWIST = 0, MAX_TWIST = 5)
