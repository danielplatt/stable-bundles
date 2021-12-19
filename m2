https://www.unimelb-macaulay2.cloud.edu.au/#browse
i1 : S = QQ[a..d];
i2 : R = S/(a^4+b^4+c^4+d^4);
i3 : X = Proj R
o3 =  X
o3 :  ProjectiveVariety
i4 : HH^0(OO_X)
o4 =  Q
1
o4 :  Q-module, free

problem: divisors on R have no rational points
Matthias Schütt, Tetsuji Shioda, and Ronald van Luijk, Lines on Fermat surfaces