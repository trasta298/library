mod = 10**9+7
l = 10**6
fac = [1]*l
facr = [1]*l
 
for i in range(l-1):
    fac[i+1] = fac[i]*(i+1)%mod
facr[l-1] = pow(fac[l-1],mod - 2,mod)
for i in range(1,l)[::-1]:
    facr[i-1] = facr[i]*i%mod
 
def cmb(N,K):
    return fac[N]*facr[N-K]%mod*facr[K]%mod