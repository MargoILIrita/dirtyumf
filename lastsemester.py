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


def ppi(hr, ht):
    return 1+ 2*gamma(ht, hr) + psi(ht)


def uui(ht, hr, ri):
    return ht/(2*hr*ri) - gamma(ht, hr)


def qqi(ht, hr, ri):
    return gamma(ht,hr) + ht/(2*hr*ri)


def ssi(w, ri, ht):
    return w + mm.da['betta']*ht*ir(ri)/mm.da['c']


def uI(hr, ht, ri):
    return 1 + 2*gamma(ht, hr) + psi(ht)


def pI(ht, hr, ri):
    return 2*gamma(ht, hr)


def sI(w, ri, ht):
    return w + mm.da['betta']*ht*ir(ri)/mm.da['c']


def alfa0(ht, hr):
    return q0(ht, hr)/p0(ht, hr)


def betta0(w, ht, hr):
    return s0(w, ht)/p0(ht, hr)


#alfa j
#ri для j-1, alf для j-1
def alfaj(ht, hr, ri, alfa):
    return qqi(ht, hr, ri)/( ppi(ht, ht) + uui(ht, hr, ri)* alfa)



#b k-1 j
#ri для j-1, alf для j-1, betta для j-1
def bettaj(w, ri, ht, hr, betta, alfa):
    u = uui(ht, hr, ri)
    return (ssi(w, ri, ht) - u* betta)/(ppi(hr, ht) + alfa*u)


#w k I
#betta for I k-1, alf for I
def wI(w, ri, ht, hr, betta, alfa):
    u = uI(hr, ht, ri)
    return (sI(w, ri, ht) - u*betta)/(pI(ht, hr, ri) + alfa*u)



#w k m
#bett for m+1 k, alf for m+1, w for m+1 k
def wm(alf, bett, w):
    return alf*w + bett


def straight_run(ht, hr, I, ris, ws):
    alfas = []
    bettas = []
    alfas.append(alfa0(ht, hr))
    bettas.append(betta0(ws[0], ht, hr))
    for j in range(1,I-1,1):
        alfas.append(alfaj(ht, hr, ris[j], alfas[j-1]))
        bettas.append(bettaj(ws[j], ris[j], ht, hr, bettas[j-1], alfas[j-1]))
    return alfas, bettas, wI(ws[I-1],ris[I-1], ht, hr, bettas[I-2], alfas[I-2])


def back_stroke(ht, hr, I, ris, ws):
    alfas, bettas, wi = straight_run(ht, hr, I, ris, ws)
    wnew = []
    wnew.append(wi)
    for i in range(I-2, -1, -1):
        wnew.append(wm(alfas[i],bettas[i], wnew[I-i-2]))
    wn = []
    for i in range(I-1,-1,-1):
        wn.append(wnew[i])
   # print(wn)
    return wn

def allinone(ht, hr, time=100):
    t = []
    I = int(mm.da['R']/hr)
    K = int(time/ht)
    for i in range(I):
        t.append(0)
    w = [t,]
    ris = [x for x in numpy.arange(0,mm.da['R'],hr)]
    for k in range(1, K, 1):
        w.append(back_stroke(ht,hr,I, ris,w[k-1]))
    return w



#a = allinone(1, 0.1)
#b = []
#for t in numpy.arange(100):
#   b.append([mm.u(step, t, 0.01) for step in numpy.arange(0, 5, 0.1)])

'''x = [step for step in numpy.arange(0, 5, 0.1)]
y1 = [mm.u(step,5, 0.01) for step in x]
y2 = allinone(1,0.1,6)[5]

ln0, ln1 = mpl.plot(x, y1, x, y2)
mpl.legend((ln0, ln1),('Аналитическое','Численное'))
mpl.grid()
mpl.show()'''
