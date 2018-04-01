import math

from plotly.utils import numpy

import mathmethods as mm

def ir(ri):
    if(0 <= ri <= mm.da['a']):
        return mm.da['P']/(math.pi*mm.da['a']**2)
    return 0


def psi():
    return mm.da['k']/mm.da['c']


def gamma():
    return 2*mm.da['alf']/(mm.da['c']*mm.da['l'])


def fi(ri):
    return mm.da['betta']*ir(ri)/mm.da['c']


def p0(ht, hr):
    return 1 - (4*psi()*ht/hr**2) - gamma()*ht


def q0(ht, hr):
    return 4*psi()*ht/hr**2


def s0(w, ht):
    return w + fi(0)*ht


def ppi(hr, ht):
    return 1+ 2*psi()*ht/(hr**2) + gamma()*ht


def uui(ht, hr, ri):
    return ht*psi()/(2*ri*hr) - psi()*ht/hr**2


def qqi(ht, hr, ri):
    return psi()*ht/hr**2 + psi()*ht/(2*ri*hr)


def ssi(w, ri, ht):
    return w + fi(ri)*ht


def uI(hr, ht):
    return 2*psi()*ht/hr**2


def pI(ht, hr):
    return 1+2*psi()*ht/hr**2 + gamma()*ht


def sI(w, ri, ht):
    return w + fi(5)*ht


def alfa1(ht, hr):
    return q0(ht, hr)/p0(ht, hr)


def betta1(w, ht, hr):
    return s0(w, ht)/p0(ht, hr)


#alfa j
#ri для j-1, alf для j-1
def alfaj(q, p, u, al):
    return q/(p-u*al)


#b k-1 j
#ri для j-1, alf для j-1, betta для j-1
def bettaj(s, u, bet, p, al):
    return (s+u*bet)/(p-u*al)


#w k I
#betta for I k-1, alf for I
def wI(w, ri, ht, hr, bettaI, alf):
    return (sI(w,ri,ht) - uI(hr,ht)*bettaI)/(pI(ht, hr)-uI(hr, ht)*alf)


#w k m
#bett for m+1 k, alf for m+1, w for m+1 k
def wm(alf, bett, w):
    return alf*w + bett


def straight_run(ht, hr, I, ris, ws):
    ss = []
    ps = []
    qs = []
    for i in range(I):
        if i == 0:
            ss.append(s0(ws[0],ht))
            ps.append(p0(ht, hr))
            qs.append(q0(ht,hr))
        elif i == I-1:
            ss.append(sI(ws[i], ris[i], ht))
            ps.append(pI(ht,hr))
            qs.append(qqi(ht, hr, ris[i]))
        else:
            ss.append(ssi(ws[i],ris[i],ht))
            ps.append(ppi(hr,ht))
            qs.append(qqi(ht,hr,ris[i]))
    us = []
    alfas = []
    bettas = []
    alfas.append(alfa1(ht, hr))
    bettas.append(betta1(ws[0], ht, hr))
    us.append(uui(hr,ht,ris[1]))
    for j in range(1,I,1):
        i = j-1
        alfas.append(alfaj(qs[j], ps[j], us[i], alfas[i]))
        bettas.append(bettaj(ss[j],us[i], bettas[i], ps[j], alfas[i]))
        us.append(uui(hr, ht, ris[j]))
    return alfas, bettas


def back_stroke(ht, hr, I, ris, ws):
    alfas, bettas = straight_run(ht, hr, I, ris, ws)
    wnew = []
    wnew.append(wI(ws[I-1],ris[I-1], ht, hr, bettas[I-1], alfas[I-1]))
    for i in range(I-2, -1, -1):
        wnew.append(wm(alfas[i],bettas[i], wnew[I-i-2]))
    wn = []
    for i in range(I-1,-1,-1):
        wn.append(wnew[i])
    print(wn)
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






