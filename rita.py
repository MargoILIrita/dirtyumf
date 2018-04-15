import math
import matplotlib.pyplot as mpl

from plotly.utils import numpy

import mathmethods as mm

def ir(ri):
    if(0 <= ri <= mm.da['a']):
        a = mm.da['P']/(math.pi*mm.da['a']**2)
        return a
    return 0


def psi(ht):
    return 2 * mm.da['alf'] * ht / (mm.da['c'] * mm.da['l'])


def gamma(ht, hr):
    return mm.da['k'] * ht / (mm.da['c'] * hr**2)


def p0(ht, hr):
    return 1 + 4*gamma(ht,hr) + psi(ht)


def q0(ht, hr):
    return 4*gamma(ht,hr)


def s0(w, ht):
    return w + mm.da['betta']*ht*ir(0)/mm.da['c']


def ppi(hr, ht, ri):
    return 1+ 2*gamma(ht, hr) + psi(ht) - gamma(ht, hr)*hr/ri


def uui(ht, hr, ri):
    return gamma(ht, hr) - gamma(ht, hr)*hr/ri


def qqi(ht, hr, ri):
    return gamma(ht,hr)


def ssi(w, ri, ht):
    return w + mm.da['betta']*ht*ir(ri)/mm.da['c']


def uI(hr, ht, ri):
    return gamma(ht,hr) - gamma(ht, hr) * hr/ri


def pI(ht, hr, ri):
    return 1 + gamma(ht, hr) - gamma(ht, hr)*hr/ri + psi(ht)


def sI(w, ri, ht):
    return w + mm.da['betta']*ht*ir(ri)/mm.da['c']

#w k I
#betta for I k-1, alf for I
def wI(w, ri, ht, hr, betta, alfa):
    u = uI(hr, ht, ri)
    return (sI(w, ri, ht) - u*betta)/(pI(ht, hr, ri) + alfa*u)



#w k m
#bett for m+1 k, alf for m+1, w for m+1 k
def wm(alf, bett, w):
    return alf*w + bett
