import math
import time
import numpy as np

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


def pp0(ht, hr):
    return 1 - 4*gamma(ht, hr) - psi(ht)


def ppi(ht, hr, ri):
    return 1 - 2*gamma(ht, hr) + gamma(ht, hr) * hr/ri - psi(ht)


def uui(ht, hr, ri):
    return gamma(ht, hr) - gamma(ht, hr)*hr/ri


def ss0(ht):
    return mm.da['betta']*ht*ir(0)/mm.da['c']

def ssi(ht, ri):
    return mm.da['betta']*ht*ir(ri)/mm.da['c']


def w0(w0, w1, ht, hr):
    return w0*pp0(ht, hr) + w1*4*gamma(ht, hr) + ss0(ht)


def wi(wm, wi, wp, ri, ht, hr):
    return wi*ppi(ht, hr, ri) + wm*uui(ht,hr,ri) + wp*gamma(ht, hr) + ssi(ht, ri)


def wI(hr, w):
    return hr*w/mm.da['k']

def all(w, ht, hr, ris):
    len = ris.__len__()
    cur = [w0(w[0], w[1], ht, hr),]
    for i in range(1, len-1, 1):
        cur.append(wi(w[i-1], w[i], w[i+1], ris[i], ht, hr))
    cur.append(wI(hr, w[len-1]))
    return cur

def xOy(args):
    tt = time.time()
    stepr, stept, riarr = args[0], args[1], args[2]
    res = [np.zeros((riarr.__len__(), 1)), ]
    for k in range(1, 100, stept):
        res.append(all(res[k - 1], stept, stepr, riarr))
    print('finish process olya' + ' {0:.2f}'.format(time.time()-tt))
    return res