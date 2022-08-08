from sympy.combinatorics.named_groups import SymmetricGroup
import itertools
from tqdm import tqdm


def tuplefy(x: int):
    return (x//100, (x//10)%10, x%10)

def get_phi():
    return {(False, tuplefy(123)), (False, tuplefy(145)), (False, tuplefy(167)), (False, tuplefy(246)),
            (True, tuplefy(257)), (True, tuplefy(347)), (True, tuplefy(356))} # this is a set

def permutation_list_to_dict(permutation_list):
    dictionary = {}
    for original_number, new_number in enumerate(permutation_list):
        dictionary[original_number+1] = new_number+1
    return dictionary

def perform_bubble_sort(tuple_to_be_sorted):
    # https://www.faqcode4u.com/faq/648262/python-bubble-sort-list-with-swap-count
    swapcount = 0
    temporary_list = list(tuple_to_be_sorted)
    for j in range(len(temporary_list)):
        for i in range(1, len(temporary_list) - j):
            if temporary_list[i - 1] > temporary_list[i]:
                swapcount += 1
                temporary_list[i - 1], temporary_list[i] = temporary_list[i], temporary_list[i - 1]
    return tuple(temporary_list), swapcount

def permute_primitive_alternating_tensor(tensor, permutation_dict):
    # first apply permutation
    permuted_vector = [permutation_dict[k] for k in tensor[1]]

    # then sort again
    sorted_vector, number_of_swaps = perform_bubble_sort(permuted_vector)

    return (bool(number_of_swaps%2) ^ tensor[0], sorted_vector)

def permute_composite_alternating_tensor(tensor, permutation_dict):
    return set([permute_primitive_alternating_tensor(t, permutation_dict) for t in tensor])

def get_all_reflections():
    return itertools.product([False, True], repeat=7)

def apply_reflection_to_primitive_tensor(reflection, tensor):
    sign_count = 0
    for component in tensor[1]:
        if reflection[component-1]:
            sign_count += 1
    return (bool(sign_count%2) ^ tensor[0], tensor[1])

def apply_reflection_to_composite_tensor(reflection, tensor):
    return set([apply_reflection_to_primitive_tensor(reflection, t) for t in tensor])

def find_phi_stabilisers():
    automorphism_count = 0
    gamma_automorphism_count = 0
    phi = get_phi()
    G = SymmetricGroup(7)
    all_permutations = list(G.generate_schreier_sims(af=True))
    for permutation in all_permutations:
        for reflection in get_all_reflections():
            if phi == permute_composite_alternating_tensor(
                    apply_reflection_to_composite_tensor(
                        reflection,
                        phi),
                    permutation_list_to_dict(permutation)
                    ):
                automorphism_count += 1
                print(f'{automorphism_count}: Permutation/reflection {[x+1 for x in permutation], reflection} preserves phi. ', end='')

                # phi is preserved, now can do detailed checks
                # Detailed check 1: does this map descend to T^7/Gamma (check "weak commuting")
                # if weak_check_commuting_with_Gamma(reflection, permutation):
                #     print('* weakly commutes with Gamma')
                #     gamma_automorphism_count += 1
                # else:
                #     print('')

                # Detailed check 2: if composing this automorphism with a translation, can it be made
                # to be descending to T^7/Gamma (this is more general than the previous question)

                has_compatible_translation = False
                for translation in get_all_candidate_translations():
                    if weak_check_commuting_with_Gamma_with_translation(reflection, permutation, translation):
                        print(f'With translation{translation([0,0,0,0,0,0,0])} descends to T^7/Gamma!')
                        gamma_automorphism_count += 1
                        has_compatible_translation = True
                if not has_compatible_translation:
                    print('No translation can make this descend to T^7/Gamma')

    print(f'Found {automorphism_count} automorphisms in total')
    print(f'Of them, {gamma_automorphism_count} commute with Gamma')

def get_all_candidate_translations():
    translations_as_vectors = itertools.product([0, 1/4, 2/4, 3/4], repeat=7)
    return [
        convert_translation_vector_to_translation_function(vec) for vec in translations_as_vectors
    ]

def convert_translation_vector_to_translation_function(vector):
    return lambda x: [
        x[k]+vector[k] for k in range(len(vector))
    ]

def apply_reflection_to_point(reflection, point):
    return [-coordinate if reflect_coordinate else coordinate for (coordinate, reflect_coordinate) in zip(point, reflection)]

def apply_permutation_to_point(permutation, point):
    '''
    Applies a permutation to a point by permuting its coordinates

    :param permutation: Something like [0, 1, 3, 2, 4, 5, 6], i.e. numbers from 0 to 6
    :param point: A vector of length 7
    :return: The encoded permutation applied to the vector
    '''
    return [point[permuted_index] for permuted_index in permutation]

def alpha(point):
    return [point[0], point[1], point[2], -point[3], -point[4], -point[5], -point[6]]

def beta(point):
    return [point[0], -point[1], -point[2], point[3], point[4], 1/2-point[5], -point[6]]

def gamma(point):
    return [-point[0], point[1], -point[2], point[3], 1/2-point[4], point[5], 1/2-point[6]]

def check_commuting_with_Gamma(reflection, permutation):
    '''
    Tests if gamma(permutation(reflection(.)))=permutation(reflection(gamma))) for each element gamma in Gamma.
    '''
    test_point = [0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07]
    if apply_permutation_to_point(
            permutation,
            apply_reflection_to_point(
                reflection,
                alpha(test_point)
            )
    ) == alpha(
        apply_permutation_to_point(
            permutation,
            apply_reflection_to_point(
                reflection,
                test_point
            )
        )
    ) and \
            apply_permutation_to_point(
            permutation,
            apply_reflection_to_point(
                reflection,
                beta(test_point)
            )
    ) == beta(
        apply_permutation_to_point(
            permutation,
            apply_reflection_to_point(
                reflection,
                test_point
            )
        )
    ) and \
            apply_permutation_to_point(
            permutation,
            apply_reflection_to_point(
                reflection,
                gamma(test_point)
            )
    ) == gamma(
        apply_permutation_to_point(
            permutation,
            apply_reflection_to_point(
                reflection,
                test_point
            )
        )
    ):
        return True
    else:
        False

def get_Gamma_group():
    return [
        lambda x: x,
        alpha,
        beta,
        gamma,
        lambda x: alpha(beta(x)),
        lambda x: alpha(gamma(x)),
        lambda x: beta(gamma(x)),
        lambda x: alpha(beta(gamma(x)))
    ]

def equal_mod_one(x, y):
    for x_coord, y_coord in zip(x, y):
        if round(x_coord%1, 2) != round(y_coord%1, 2):
            return False
    return True

def weak_check_commuting_with_Gamma(reflection, permutation):
    '''
    Tests if for all gamma1 in Gamma there exists gamma2 in Gamma such that
    gamma2(permutation(reflection(.)))=permutation(reflection(gamma1))). This is exactly the condition
    for the map permutation(reflection(.)) defined on T^7 to descend to T^7/Gamma.
    '''
    test_point = [0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07]
    for g in get_Gamma_group():
        g_okay = False
        for h in get_Gamma_group():
            if equal_mod_one(
                    apply_permutation_to_point(permutation, apply_reflection_to_point(reflection, g(test_point))),
                    h(apply_permutation_to_point(permutation, apply_reflection_to_point(reflection, test_point)))
            ):
                g_okay = True
        if not g_okay:
            return False
    return True

def test_weak_check_commuting_with_Gamma():
    reflection = (False, False, False, False, False, False, False)
    permutation = [0, 1, 2, 3, 4, 5, 6]
    for translation in get_all_candidate_translations():
        if weak_check_commuting_with_Gamma_with_translation(reflection, permutation, translation):
            print(f'With translation{translation([0, 0, 0, 0, 0, 0, 0])} descends to T^7/Gamma!')
        else:
            # print(f'With translation{translation([0, 0, 0, 0, 0, 0, 0])} NOT descend to T^7/Gamma!')
            pass

def weak_check_commuting_with_Gamma_with_translation(reflection, permutation, translation):
    '''
    Tests if for all gamma1 in Gamma there exists gamma2 in Gamma such that
    gamma2(permutation(reflection(.)))=permutation(reflection(gamma1))). This is exactly the condition
    for the map permutation(reflection(.)) defined on T^7 to descend to T^7/Gamma.
    '''
    test_point = [0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07]
    for g in get_Gamma_group():
        g_okay = False
        for num, h in enumerate(get_Gamma_group()):
            # print(num)
            # input()
            # print(f'g={g(test_point)}')
            # print(f'h={h(test_point)}')
            # print(translation(apply_permutation_to_point(permutation, apply_reflection_to_point(reflection, g(test_point)))))
            # print(h(translation(apply_permutation_to_point(permutation, apply_reflection_to_point(reflection, test_point)))))
            if equal_mod_one(
                    translation(apply_permutation_to_point(permutation, apply_reflection_to_point(reflection, g(test_point)))),
                    h(translation(apply_permutation_to_point(permutation, apply_reflection_to_point(reflection, test_point))))
            ):
                g_okay = True
        if not g_okay:
            # print(f'Problem element: g={g(test_point)}')
            # input()
            return False
    return True


if __name__ == '__main__':
    # tensor = (True, [1,2,7])
    # permutation_dict = permutation_list_to_dict([2,1,3,4,5,6,7])
    # print(permute_primitive_alternating_tensor(tensor, permutation_dict))

    # test_weak_check_commuting_with_Gamma()
    # exit()

    find_phi_stabilisers()
