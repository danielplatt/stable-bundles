from itertools import combinations_with_replacement


def first_chern_of_free_bundle(bundle: list) -> int:
    return sum(bundle)

def second_chern_of_free_bundle(bundle: list) -> int:
    chern = 0
    for k in range(len(bundle)):
        chern += (1/2)*2*sum([bundle[k]*i for i in bundle[k+1:]])
    return chern

def rank_of_monad(B: list, C: list) -> int:
    return len(B)-len(C)

def first_chern_of_monad(B: list, C: list) -> int:
    return first_chern_of_free_bundle(B)-first_chern_of_free_bundle(C)

def second_chern_of_monad(B: list, C: list) -> int:
    return int(first_chern_of_monad(B, C)*first_chern_of_free_bundle(B)+\
           second_chern_of_free_bundle(C)-\
           second_chern_of_free_bundle(B))

def main():
    B = [-1, -2, -3]
    C = [2, 1]
    # print(first_chern_of_free_bundle(B))
    # print(second_chern_of_free_bundle(B))
    # print(first_chern_of_monad(B,C))
    # print(second_chern_of_monad(B, C))

    MAX_RANK_B = 3
    MIN_TWIST = 0
    MAX_TWIST = 50
    MIN_C2 = 1

    for rB in range(2, MAX_RANK_B+1):
        rC = rB - 2
        for B in combinations_with_replacement(range(MIN_TWIST, MAX_TWIST+1), rB):
            for C in combinations_with_replacement(range(max(B), MAX_TWIST+1), rC):
                # print(B,C)
                # good chern class?
                c2 = second_chern_of_monad(B, C)
                c1 = first_chern_of_monad(B, C)
                if -4*c2+c1 == -6 and c2>MIN_C2:
                    print('c2=%s. B=%s, C=%s' % (c2, B, C))

    # for rB in range(MAX_RANK_B):
    #     rC = rB-2
    #     B = [MIN_TWIST for _ in range(rB)]
    #     C = [MIN_TWIST for _ in range(rC)]
    #     for i in range(rB):
    #         for k in range(min(B), MAX_TWIST+1): # making sure twists are in ascending order
    #             B[i] = k






if __name__ == '__main__':
    main()