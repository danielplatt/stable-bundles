needsPackage "TateOnProducts";
(S,E) = productOfProjectiveSpaces{1,1};
F1 = ker matrix {{x_(0,0),x_(0,1),x_(1,0),x_(1,1)}}
low={-5,-5}; high={5,5};
cohomologyMatrix(F1,low,high)
cohomologyMatrix(exteriorPower(2,F1),low,high)

-- computation on P1x{z}
needsPackage "TateOnProducts"
(S,E) = productOfProjectiveSpaces{1,0};
F1 = ker matrix {{x_(0,0),x_(0,1),0,1}}
low = {-5,0};high={5,0};
cohomologyMatrix(F1,low,high)

F2 = ker matrix {{x_(0,0)*x_(0,0),x_(0,1)*x_(0,1),x_(1,0)*x_(1,0),x_(1,1)*x_(1,1)}}
low={-5,-5}; high={5,5};
cohomologyMatrix(F2,low,high)
low={-3,-3}; high={6,6};
cohomologyMatrix(exteriorPower(2,F2),low,high)

-- computation on P1x{[0:1]}
needsPackage "TateOnProducts"
(S,E) = productOfProjectiveSpaces{1,0};
F2 = ker matrix {{x_(0,0)*x_(0,0),x_(0,1)*x_(0,1),0,1}}
low = {-5,0};high={6,0};
cohomologyMatrix(F2,low,high)


