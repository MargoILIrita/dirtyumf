import math
import mathmethods as mm

def ir(ri):
    if(0 <= ri <= mm.da['a']):
        return mm.da['P']/(math.pi*mm.da['a'])
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


def s0(w, ri, ht):
    return w + fi(ri)*ht


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
    return w + fi(ri)*ht


def alfa1(ht, hr):
    return q0(ht, hr)/p0(ht, hr)


def betta1(w, ri, ht, hr):
    return s0(w, ri, ht)/p0(ht, hr)


#alfa j
#ri для j-1, alf для j-1
def alfaj(ht,hr,ri,alf):
    return qqi(ht,hr,ri)/(uui(ht,hr,ri)*alf)


#b k-1 j
#ri1 для j-1, ri для j, alf для j, betta для j-1
def bettaj(w, ri1, ht, hr, betta, ri, alf):
    return (ssi(w,ri1, ht) + uui(ht,hr,ri1)*betta)/(ppi(hr,ht) - uui(ht,hr,ri)*alf)


#w k I
#betta for I k-1, alf for I
def wI(w, ri, ht, hr, bettaI, alf):
    return (sI(w,ri,ht) - uI(hr,ht)*bettaI)/(pI(ht, hr)-uI(hr, ht)*alf)


#w k m
#bett for m+1 k, alf for m+1, w for m+1 k
def wm(ht, hr, ri, alf, bett, w):
    return alfaj(ht, hr, ri, alf)*w + bett


