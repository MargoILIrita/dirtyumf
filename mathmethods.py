import scipy.special as spc
import scipy as sp
import numpy as np
import matplotlib.pyplot as mpl

__bessel0 = [0,]
temp = spc.jn_zeros(1, 10000000)
for t in temp:
    __bessel0.append(t)

def bessel0(n):
    return __bessel0[n]

da = {'R': 5, 'l': 0.5, 'k': 0.065, 'alf': 0.01,
       'c' : 1.84, 'betta': 0.004,
      'P' : 40,'a': 1}

def updateDA(dan):
    da['R'] = dan['R']
    da['l'] = dan['l']
    da['k'] = dan['k']
    da['alf'] = dan['alf']
    da['c'] = dan['c']
    da['betta'] = dan['betta']
    da['P'] = dan['P']
    da['a'] = dan['a']

def rt(n):
    ayyy = 50*0.5815169517*da['betta']*da['P']*2**(1/2)
    return ayyy/(da['R']*(n*sp.pi)**(1/2))


def besfun(n):
    mn = bessel0(n)
    j0 = spc.j0(mn)
    j1 = spc.j1(mn/5)
    return j1/j0**2

def bn(n):
    b = 10*da['betta']*da['P']
    b/= sp.pi*da['c']*da['R']
    b/=bessel0(n)
    b*=besfun(n)
    return b

def gamma(n):
    g = (-1*bessel0(n)**(2)*da['k'])/(da['c']*da['R']**2)
    g-=2*da['alf']/(da['c']*da['l'])
    return g

def expY(n, t):
   return sp.exp(gamma(n)*t) - 1


def u(r,t, eco, dan=None):
    if dan != None:
        updateDA(dan)
    u = da['betta']*da['P']*expY(0,t)*spc.j0(0)
    u /= gamma(0)*da['c']*np.pi*da['R']**2
    for i in np.arange(1,100,1):
        mn = bessel0(i)
        u += bn(i) * expY(i, t) * spc.j0(mn * r / da['R']) / gamma(i)
    return u

def graphR():
    mpl.figure(0)
    res0, res1, res2, res3, res4, res5 = [], [], [], [], [], []
    x = [t for t in range(100)]
    res0 = [u(0, t,0.1) for t in x]
    res1 = [u(1, t, 0.1) for t in x]
    res2 = [u(2, t,0.1) for t in x]
    res3 = [u(3, t, 0.1) for t in x]
    res4 = [u(4, t,0.1) for t in x]
    ln0, ln1, ln2, ln3, ln4 = mpl.plot(x, res0, x, res1, x, res2, x, res3, x, res4)
    mpl.legend((ln0, ln1, ln2, ln3, ln4), ('r=0','r=1','r=2','r=3','r=4'))
    mpl.grid()
   # mpl.plot(x, res0)


def graphT():
    mpl.figure(1)
    res0, res1, res2, res3, res4, res5 = [], [], [], [], [], []
    x = [t for t in np.arange(0,5,0.1)]
    res0 = [u(t, 0,0.1) for t in x]
    res1 = [u(t, 20,0.1) for t in x]
    res2 = [u(t, 40,0.1) for t in x]
    res3 = [u(t, 60,0.1) for t in x]
    res4 = [u(t, 80,0.1) for t in x]
    ln0, ln1, ln2, ln3, ln4 = mpl.plot(x, res0, x, res1, x, res2, x, res3, x, res4)
    mpl.legend((ln0, ln1, ln2, ln3, ln4), ('t=0','t=20','t=40','t=60','t=80'))
   # mpl.plot(x, res0)
    '''x = [t for t in np.arange(0, 5, 0.1)]
    res0 = [u(t, 0) for t in x]
    res2 = [u(t, 40) for t in x]
    ln0, ln1 = mpl.plot(x, res0, x, res2)
    mpl.legend((ln0, ln1), ('t=0', 't=40'))'''
    mpl.grid()

def getparams():
    return da

'''graphR()
graphT()
mpl.show()'''
