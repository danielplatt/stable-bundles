R = QQ[x,y,z,w]/(-x*y^3+...)
X = Proj R
-- X is a K3 surface

F = sheaf ker matrix {{a, b, c, d}, {a^2, b^2, c^2, d^2}}
-- Macaulay2 automatically takes F to be a subsheaf of O(-2)^4
-- Chern class c1=(-2)*4-(-1+0)=-7

Fdual = dual F
-- Degree ("first Chern class") +7

Fdualnormed = Fdual(-4)
-- Degree ("first Chern class") -1

-- Now, for Hoppe's criterion need to check:
-- HH^0(Fdualnormed**OO(B))=0 for all B with deg(B)<=1/2

-- here comes the check
needsPackage "Divisor";
-- hyperplane class
H = divisor(ideal(x))

-- second divisor C (Lemma 7.2)
C = ?????

-- then have: Pic(X)=<H,C> (Proposition 7.3)
-- HH^0(Fdualnormed**(sheaf OO(-D)))

-- if D was a generator of Pic(X), then this would prove that F(4) is stable. But D is just an arbitrary divisor of degree 5, so this doesn't prove that F(4) is stable.