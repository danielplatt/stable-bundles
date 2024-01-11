import itertools


def mukai_vectors_on_polarised_k3(maxrank=6, maxc1=10, maxc2=10):
    '''Find rank r and Chern classes c1, c2 which give
    virtual dimension 0. Here, c1 and c2 are given as
    integer numbers meaning multiples of the polarisation
    of the K3 surface.

    There may be bundles whose Chern classes are not
    multiples of the polarisation. For example if the
    K3 is a branched double cover and the bundle is a pullback
    from the base.'''
    print('Mukai vectors (r, c1, c2) for polarised K3s')
    for r in range(2,maxrank):
        for c1 in range(-maxc1+1, maxc1):
            for c2 in range(-maxc2+1, maxc2):
                virtual_dimension = 2*r*c2-(r-1)*(c1**2)-2*(r**2-1)
                if virtual_dimension == 0:
                    print(f'({r}, {c1}, {c2})')


def mukai_vectors_on_double_p2(maxrank=6, maxc1=10, maxc2=10):
    '''Find rank r and Chern classes c1, c2 which give
    virtual dimension 0.

    Warning: Here, c1 and c2 are given as
    integer numbers meaning multiples of the hyperplane
    section on P2, not the K3 surface!

    The Chern classes of the pullback bundle on the K3
    are then not multiples of the polarisation of the K3,
    but are multiples of the pullback of the hyperplane
    section from P2.'''
    print('Mukai vectors (r, c1, c2) on branched double P2s, \nwhere c1 and c2 denotes the Chern classes on P2!')
    for r in range(2,maxrank):
        for c1 in range(-maxc1+1, maxc1):
            for c2 in range(-maxc2+1, maxc2):
                virtual_dimension = 2 * r * (2*c2) - (r - 1) * 2*(c1 ** 2) - 2 * (r ** 2 - 1)
                if virtual_dimension == 0:
                    print(f'({r}, {c1}, {c2})', end='')
                    if r==2 and c1==3 and c2==3:
                        print(' <-- tangent bundle TP2')
                    else:
                        print('')


def mukai_vectors_on_double_p1_p1(maxrank=6, maxc1=3, maxc2=10):
    '''Find rank r and Chern classes c1, c2 which give
    virtual dimension 0.

    Warning: Here, c1 is given as a pair of integers,
    denoting a sum of the two generators of H2(P1 x P1).
    c2 is given as a single
    integer meaning multiples of the hyperplane
    generator of H4(P1 x P1).

    The Chern classes of the pullback bundle on the K3
    are then not multiples of the polarisation of the K3,
    but pullbacks of the Chern classes from P1 x P1.'''
    print('Mukai vectors (r, c1, c2) on branched double P1xP1s, \nwhere c1 and c2 denotes the Chern classes on P1xP1!')
    for r in range(2,maxrank):
        for c1 in itertools.product(range(-maxc1+1, maxc1), range(-maxc1+1, maxc1)):
            c1_squared = c1[0]*c1[1]
            for c2 in range(-maxc2+1, maxc2):
                virtual_dimension = 2 * r * (2*c2) - (r - 1) * 2*(c1_squared) - 2 * (r ** 2 - 1)
                if virtual_dimension == 0:
                    print(f'({r}, {c1}, {c2})')


if __name__ == '__main__':
    print('Finding bundles with virtual dimension 0')
    mukai_vectors_on_polarised_k3(maxrank=6, maxc1=10, maxc2=10)
    mukai_vectors_on_double_p2(maxrank=6, maxc1=10, maxc2=10)
    mukai_vectors_on_double_p1_p1(maxrank=6, maxc1=3, maxc2=10)
