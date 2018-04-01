import  mathmethods as mm
import numpy as np
import  scipy as sp
import scipy.special

d = mm.da

def a(n):
    if n > 10000000:
        return 0
    mn = mm.bessel0(i)
    return mm.bn(i) * mm.expY(n, 12) * sp.special.j0(mn * 2 / d['R']) / mm.gamma(n)


def u(y):
    u = -1*d['c']*d['l']*d['betta']*d['P'] * (sp.exp(-2*d['alf']*12/(d['c']*d['l'])) - 1)/(25*sp.pi*2*d['alf']*d['a']**2)
    for i in np.arange(1,y,1):
        u += a(i)
    return u


def nt(eps):
    RT = mm.rt(1)
    nx=1
    while(RT > eps):
        nx+=1
        RT = mm.rt(nx)
    return nx


def npp(eps, nz):
    start = u(nz)
    stop = start-a(nz-1)
    while(nz>0) and (eps > abs(start-stop)):
     nz-=1
     stop-=a(nz-1)
    return nz


for i in range(1,5,1):
    eps = 10**(-i)
    bt =nt(eps)
    print("Eps {0} Nteory {1} Nprac {2}".format(eps, bt, npp(eps, bt)))

