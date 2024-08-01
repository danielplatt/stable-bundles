R = QQ[x,y,z]
X = Proj(R)
F = sheaf ker matrix {{x^20, y^20, z^20}}
--c1=-2
--so c1(F(1))=0
HH^0(F ** OO_X(1))
--0
--so by Hoppe criterion: F is stable

G = sheaf ker matrix {{x^2,x*y,x*z,y^2,y*z,z^2}}
--c1(G)=c1(O(0))-c1(O(2))=-2
--so c1(G(0)) is normed, because in range {-4,-3,-2,-1,0}
HH^0(G)
--0
--so by Hoppe criterion: F is stable
