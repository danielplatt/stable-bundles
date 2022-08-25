R = QQ[x,y,z]
F = sheaf ker matrix {{x, y, z}}
K = F(1)
-- The line F = F(1) is needed to define K as a subsheaf of O^3 rather than O(1)^3
Kdual = dual K
Kdualnormed = Kdual(-1)
HH^0(Kdualnormed)
-- output
-- o6 =  0
-- o6 :  Q-module