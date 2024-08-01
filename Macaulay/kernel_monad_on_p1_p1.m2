needsPackage "SegreClasses"
R = makeProductRing(QQ,{1,1})

degrees R
--{{1,0},{1,0},{0,1},{0,1}}

gens R
--{a,b,c,d}

X = Proj R
-- X=P^1xP^1

F = sheaf ker matrix {{a*c,a*d,b*c,b*d}}
-- Macaulay2 cannot compute sheaf cohomology if degrees of generators are given as
-- length 2 lists.
-- HH^0(F) generates "/usr/share/Macaulay2/Varieties.m2:502:38:(3): error: expected degree length 1"
HH^0(F)

-----------------

-- So we transform everything into calculations on the quadric using the Segre embedding
-- s: P^1xP^1 -> P^3, (a:b),(c:d)->(ac,ad,bc,bd)
-- write x=ac,y=ad,z=bc,w=bd

R = QQ[x,y,z,w]/(x*w-y*z)
X = Proj R
F = sheaf ker matrix {{x,y,z,w}}
HH^0(F)

-----------------

-- on the quadric it's hard to write monads with the bundles O(m,n)
-- alternative approach

needsPackage "TateOnProducts"
(S,E) = productOfProjectiveSpaces{1,1}
M = S^1
-- this is the coordinate ring
low = {-2,-2};high={2,2};
cohomologyMatrix(M,low,high)
F = sheaf ker matrix {{x_(0,0)}}
HH^0(F)

---------
needsPackage "TateOnProducts"
(S,E) = productOfProjectiveSpaces{1,1}
F = ker matrix {{x_(0,0),x_(1,0),x_(0,1),x_(1,1)}}
low = {-2,-2};high={2,2};
cohomologyMatrix(F,low,high)
