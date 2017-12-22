import  mathmethods as mm
import numpy as np
import  scipy as sp
import scipy.special

d = mm.da

def a(n):
    mn = mm.bessel0(i)
    return mm.bn(i) * mm.expY(n, 12) * sp.special.j0(mn * 2 / d['R']) / mm.gamma(n)


def u(y):
    u = -1*d['c']*d['l']*d['betta']*d['P'] * (sp.exp(-2*d['alf']*12/(d['c']*d['l'])) - 1)/(25*sp.pi*2*d['alf']*d['a']**2)
    for i in np.arange(1,y,1):
        u += a(i)
    return u


for i in range(1,10,1):
    eps = 10**(-i)
    NT =  mm.last(i)
    NP = NT
    res = 0
    while NP>0 and res < eps:
        ai = a(NP)
        ud = u(NP-1)
        res = ai/ud
        NP-=1
    print("Eps {0} Nteory {1} Nprac {2}".format(eps, NT, NP))
