needsPackage "TateOnProducts";
(S,E) = productOfProjectiveSpaces{1,1};
generators S
degrees S
F = ker matrix {{x_(0,0)*x_(1,0),x_(0,0)*x_(1,1),x_(0,1)*x_(1,0),x_(0,1)*x_(1,1)}}
-- The graded module F is given as the image of this 4x4 matrix.
-- The notation {1,1} in front of the four rows of the matrix
-- means that the unit element "1" in the four components of the
-- target space has bi-degree (1,1). This completely specifies that
-- the matrix is a map from S^4_{\bullet + (2,2)} to S^4_{\bullet + (1,1)}.
low = {-5,-5}; high={5,5};
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