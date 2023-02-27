# stable-bundles

## Finding monad bundles on K3

0. Install Macaulay2 on your machine or run Macaulay2 code online here: https://www.unimelb-macaulay2.cloud.edu.au/#browse

1. Run the following Macaulay2 code: ```input "[PATH TO REPOSITORY]/Macaulay/trivial_example_on_projective_space.m2"```.
 This computes the zero-th cohomology of the structure sheaf O(1) on CP^2. Zero-th cohomology means space of global sections, and the global sections of O(1) are the degree one homogeneous polynomials, i.e. ```x```, ```y```, and ```z``` (the three coordinates on CP^2). That's why Macaulay2 gives the result QQ^3, i.e. a three-dimensional vector space.
   
2. ```input "[PATH TO REPOSITORY]/Macaulay/compute_tangent_bundle_cp2.m2"```. The cotangent bundle ```K``` of CP^2 fits into the Euler sequence:
 ```0 -> K -> O(-1)^3 -> O(0) -> 0```, i.e. it is the kernel of the map ```O(-1)^3 -> O(0)```. Don't really remember why I take ```(1)``` and ```(-1)``` in the code...
   
3. ```input "[PATH TO REPOSITORY]/Macaulay/compute_monad_kernel_on_K3.m2"```. Define a K3 surface, and a sheaf ```F```, take dual and normalise it (i.e. tensor it with ```O(k)``` so that is has Chern class ```0``` or ```-1```). Then compute some zero-th cohomology groups. Computations like this are necessary to check if a bundle is stable.