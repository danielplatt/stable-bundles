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
F = ker matrix {{x_(0,0),x_(0,0),x_(0,1),x_(0,1)}}
low = {-5,0};high={5,0};
cohomologyMatrix(F,low,high)

exteriorPower(2,F)
cohomologyMatrix(exteriorPower(2,F),low,high)