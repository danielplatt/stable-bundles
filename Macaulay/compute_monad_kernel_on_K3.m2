R = QQ[a,b,c,d]/(a^4+b^4+c^4+d^4)
X = Proj R
-- X is a K3 surface

F = sheaf ker matrix {{a, b, c, d}, {a^2, b^2, c^2, d^2}}
-- Macaulay2 automatically takes F to be a subsheaf of O(-2)^4
-- Chern class c1=(-2)*4-(-1+0)=-7

Fdual = dual F
-- Chern class +7

Fdualnormed = Fdual(-4)
-- Chern class -1

-- Now, for Hoppe's criterion need to check:
-- (a) HH^0(Fdualnormed(0))=0, HH^0(Fdualnormed(-1)), HH^0(Fdualnormed(-2)), ...
-- (b) HH^0(Fdualnormed**OO(B))=0 for all B with deg(B)<=1/2

-- here comes the check for (a)
HH^0(Fdualnormed)

-- here comes the check for (b)
needsPackage "Divisor";
D = divisor(ideal(a^5+b^5+c^5+d^5))
-- degree +5
HH^0(Fdualnormed**(sheaf OO(-D)))

-- if D was in Pic(X), then this would prove that F(4) is stable. But D is just an arbitrary divisor of degree 5, so this doesn't prove that F(4) is stable.