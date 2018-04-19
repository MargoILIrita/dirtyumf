import math
import time
import numpy as np

import matplotlib.pyplot as mpl

from plotly.utils import numpy

import mathmethods as mm

def ir(ri):
    if(ri <= mm.da['a']):
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

def xOy(args):
    tt = time.time()
    stepr, stept, riarr = args[0], args[1], args[2]
    res = [np.zeros((riarr.__len__(), 1)), ]
    for k in np.arange(1, 100, stept):
        len = riarr.__len__()-1
        ss = []
        j = 0
        for ri in riarr[0:len]:
            if (ri == 0):
                ss.append([s0(0, stept), ])
            else:
                ss.append([ssi(res[k-1][j], ri, stept), ])
            j += 1
        s = np.matrix(ss)
        a = np.zeros((len, len))
        a[0, 0] = p0(stept, stepr)
        a[0, 1] = -1 * q0(stept, stepr)
        a[len - 1, len - 2] = -1 * uI(stepr, stept, riarr[len - 1])
        a[len - 1, len - 1] = pI(stept, stepr, riarr[len - 1])
        for i in np.arange(1, len - 1, stept):
            a[i, i - 1] = -1 * uui(stept, stepr, riarr[i])
            a[i, i] = ppi(stepr, stept, riarr[i])
            a[i, i + 1] = -1 * qqi(stept, stepr, riarr[i])
        temp = [ele for ele in np.linalg.solve(a, s).flat]
        temp.append(temp[len-1])
        res.append(temp)

    print('finish process lilya' + ' {0:.2f}'.format(time.time()-tt))
    return res



