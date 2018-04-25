import numpy as np
import lilya
import rita
import  mathmethods as mm

def count_step_analytic(T, R):
    return [mm.u(r, T, 0.01) for r in R]


def count_analytic(R, ht):
    return [count_step_analytic(k*ht,R) for k in np.arange(0,int(100/ht),1)]


def compute_step(I, K, pervmaxl=0, isLylya=True):
    hr = 5/I
    ht = 100/K
    R = [x for x in np.arange(0,5+hr, hr)]
    analytic = np.array(count_analytic(R,ht)[1:])
    if isLylya:
        girl = np.array(lilya.xOy((hr, ht, R))[1:])
    else:
        girl = np.array(rita.xOy((hr, ht, R[0:-1]))[1:])
    delta = girl-analytic
    max = delta.max()
    print("I {0} K {1} {2}  {3} d {4}".format(I, K, "Lilia" if isLylya else "Rita" ,max, pervmaxl/max))
    return max

I = 10
K = 50
m = 0
for i in range(4):
     m = compute_step(I, K, m)
     K*=2
     I*=2

I = 5
K = 50
m = 0
for i in range(4):
    m = compute_step(I, K, m, False)
    K *= 2
    I *= 4

