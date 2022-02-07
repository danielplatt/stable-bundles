// Code to implement van Luijk's method on K3 surfaces of degree 4

// Given a homogeneous polynomial f of degree 4 and with integer coefficients,
// and a prime p, 
// the function checks that p is of good reduction for the surface S:f=0
// and then computes the rank arp and the discriminant modulo squares dp of Pic(S).
// The quantity dp is computed using the Artin--Tate formula
// so the result might not hold if p=2.

function PicNumberModp(f,p)
  P3:=ProjectiveSpace(GF(p),3);
  S:=Scheme(P3,f);
  if IsSingular(S) then
    return(0);
  end if;
  Tr:=[];
  for i in [1..10] do
    P3 := ProjectiveSpace(GF(p^i),3);
    S := Scheme(P3,f);
    Tr[i] := #Points(S) - 1 - p^(2*i);
  end for;
  R<t>:=PolynomialRing(Rationals(),1);
  cpl := FrobeniusTracesToWeilPolynomials(Tr, p, 2, 22: KnownFactor := t-p);
  cpl_2 := [wp : wp in cpl | CheckWeilPolynomial(wp,p,1: SurfDeg := 4)];
  i:=11;
  while #cpl_2 gt 1 do
    P3 := ProjectiveSpace(GF(p^i),3);
    S := Scheme(P3,f);
    Append(~Tr,#Points(S) - 1 - p^(2*i));
    cpl := FrobeniusTracesToWeilPolynomials(Tr, p, 2, 22: KnownFactor := t-p);
    cpl_2 := [wp : wp in cpl | CheckWeilPolynomial(wp,p,1: SurfDeg := 4)];
    i:=i+1;
  end while;
  wp:=cpl_2[1];
  rp:=WeilPolynomialToRankBound(wp,p);
  flag:=0;
  d:=1;
  while flag eq 0 do
    arp,dp:=ArtinTateFormula(WeilPolynomialOverFieldExtension(wp,p),p^d,1);
    if arp eq rp then
       return(<arp,SquarefreeFactorization(Numerator(dp))>); 
    end if;
    d:=d+1;
  end while; 
end function;