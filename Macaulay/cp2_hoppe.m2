needsPackage "NormalToricVarieties"
PP2 = toricProjectiveSpace 2;
ring PP2

F = sheaf ker matrix {{x0, x1, x2}}

TP = dual cotangentSheaf PP2
f0 = chern (1, TP)