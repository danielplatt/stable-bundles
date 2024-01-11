R = QQ[x,y,z]
X = Proj(R)
F = sheaf ker matrix {{x, y, z}}
K = F(1)
-- The line F = F(1) is needed to define K as a subsheaf of O^3 rather than O(1)^3
-- c1(K)=-1
-- for Hoppe criterion: check line bundles B with deg(B)<=1/2
-- so check: B= O(0), O(-1), O(-2), ...
HH^0(K ** OO_X(0))
