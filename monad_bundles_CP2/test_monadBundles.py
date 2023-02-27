from monad_bundles_CP2.monadBundles import rank_of_cohom_monad, first_chern_of_cohom_monad, second_chern_of_cohom_monad


def test_rank_of_cohom_monad():
    # from theorem 8
    # Jardim et al: HOLOMORPHIC BUNDLES FOR HIGHER DIMENSIONAL GAUGE THEORY
    for c in range(10):
        A = [-1 for _ in range(c)]
        B = [0 for _ in range(2*c+2)]
        C = [1 for _ in range(c)]
        assert rank_of_cohom_monad(A, B, C) == 2
        assert first_chern_of_cohom_monad(A, B, C) == 0
        assert second_chern_of_cohom_monad(A, B, C) == c

    tensor_offset = 1
    for c in range(10):
        A = [-1+tensor_offset for _ in range(c)]
        B = [0+tensor_offset for _ in range(2*c+2)]
        C = [1+tensor_offset for _ in range(c)]
        assert rank_of_cohom_monad(A, B, C) == 2
        assert -first_chern_of_cohom_monad(A, B, C)**2+4*second_chern_of_cohom_monad(A, B, C) == 4*c


if __name__ == '__main__':
    test_rank_of_cohom_monad()
