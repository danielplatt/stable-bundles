needsPackage "Divisor";
R = QQ[x,y,z];
D = divisor(ideal(x));
HH^0(sheaf OO(D))
-- output:
-- Q^3
-- Q-module, free