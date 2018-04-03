import math

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
    return gamma(ht, hr)*(hr/(2*ri) - 1)


def qqi(ht, hr, ri):
    return gamma(ht,hr)*(hr/(2*ri) + 1)


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
def alfaj(q, p, u, al):
    return q/(u*al + p)


#b k-1 j
#ri для j-1, alf для j-1, betta для j-1
def bettaj(s, u, bet, p, al):
    return (s - bet*u)/(u*al + p)


#w k I
#betta for I k-1, alf for I
def wI(s,u, p, bet, alf):
    return (s - u*bet)/(p+u*alf)


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
        alfas.append(alfaj(qqi(ht,hr,ris[j]),ppi(ht,ht),uui(ht,hr,ris[j]),alfas[j-1]))
        bettas.append(bettaj(ssi(ws[j], ris[j], ht),uui(ht,hr, ris[j]),bettas[j-1],ppi(hr, ht),alfas[j-1]))
    return alfas, bettas, wI(sI(ws[I-1],ris[I-1], ht),uI(hr, ht,ris[I-1]),pI(ht, hr, ris[I-1]),bettas[I-2],alfas[I-2])


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

def allinone(ht, hr):
    t = []
    I = int(mm.da['R']/hr)
    K = int(100/hr)
    for i in range(I):
        t.append(0)
    w = [t,]
    ris = [x for x in numpy.arange(0,mm.da['R'],hr)]
    for k in range(1, K, 1):
        w.append(back_stroke(ht,hr,I, ris,w[k-1]))
    return w



a = allinone(1, 0.1)
b = []
for t in numpy.arange(100):
   b.append([mm.u(step, t, 0.01) for step in numpy.arange(0, 5, 0.1)])

for i in range(100):
    print("new {0}".format(a[i]))
    print("old {0}".format(b[i]))


