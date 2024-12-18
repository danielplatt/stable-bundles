R = QQ[x,y]
X = Proj(R)
F = sheaf ker matrix {{x,x,y,y}}
{HH^0(F** OO_X(-5)), HH^0(F** OO_X(-4)), HH^0(F** OO_X(-3)), HH^0(F** OO_X(-2)), HH^0(F** OO_X(-1)), HH^0(F), HH^0(F** OO_X(1)), HH^0(F** OO_X(2)), HH^0(F** OO_X(3)), HH^0(F** OO_X(4)), HH^0(F** OO_X(5))}
F = ker matrix {{x,x,y,y}}

needsPackage "TateOnProducts"
(S,E) = productOfProjectiveSpaces{1,0}
generators S
degrees S
F = ker matrix {{x_(0,0),x_(0,0),x_(0,1),x_(0,1)}}
low = {-5,0};high={5,0};
cohomologyMatrix(F,low,high)




R = QQ[x,y]
X = Proj(R)
F = sheaf ker matrix {{x,0,y,0}}
{HH^0(F** OO_X(-5)), HH^0(F** OO_X(-4)), HH^0(F** OO_X(-3)), HH^0(F** OO_X(-2)), HH^0(F** OO_X(-1)), HH^0(F), HH^0(F** OO_X(1)), HH^0(F** OO_X(2)), HH^0(F** OO_X(3)), HH^0(F** OO_X(4)), HH^0(F** OO_X(5))}

needsPackage "TateOnProducts"
(S,E) = productOfProjectiveSpaces{1,0}
generators S
degrees S
F = ker matrix {{x_(0,0),0,x_(0,1),0}}
low = {-5,0};high={5,0};
cohomologyMatrix(F,low,high)




R = QQ[x,y]
X = Proj(R)
F = exteriorPower(2, sheaf ker matrix {{x,x,y,y}})
{HH^0(F** OO_X(-5)), HH^0(F** OO_X(-4)), HH^0(F** OO_X(-3)), HH^0(F** OO_X(-2)), HH^0(F** OO_X(-1)), HH^0(F), HH^0(F** OO_X(1)), HH^0(F** OO_X(2)), HH^0(F** OO_X(3)), HH^0(F** OO_X(4)), HH^0(F** OO_X(5))}
F = ker matrix {{x,x,y,y}}

needsPackage "TateOnProducts"
(S,E) = productOfProjectiveSpaces{1,0}
generators S
degrees S
F = exteriorPower(2, ker matrix {{x_(0,0),x_(0,0),x_(0,1),x_(0,1)}})
low = {-5,0};high={5,0};
cohomologyMatrix(F,low,high)







needsPackage "TateOnProducts"
(S,E) = productOfProjectiveSpaces{1,1}
generators S
degrees S
F = ker matrix {{x_(0,0)*x_(1,0),x_(0,0)*x_(1,1),x_(0,1)*x_(1,0),x_(0,1)*x_(1,1)}}
low = {-5,-5};high={5,5};
cohomologyMatrix(F,low,high)

exteriorPower(2,F)
cohomologyMatrix(exteriorPower(2,F),low,high)

-- computation on P1x{z}
needsPackage "TateOnProducts"
(S,E) = productOfProjectiveSpaces{1,0}
generators S
degrees S
F = ker matrix {{x_(0,0),0,x_(0,1),0}}
low = {-5,0};high={5,0};
cohomologyMatrix(F,low,high)

exteriorPower(2,F)
cohomologyMatrix(exteriorPower(2,F),low,high)









