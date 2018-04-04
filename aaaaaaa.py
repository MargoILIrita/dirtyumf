import lastsemester as ls
import numpy as np
import mathmethods as mm
import matplotlib.pyplot as mpl

ris = [st for st in np.arange(0,4.9,0.1)]

s0 = []
for ri in ris:
    if (ri == 0):
        s0.append([ls.s0(0, 1),])
    else:
        s0.append([ls.ssi(0,ri, 1),])
s = np.matrix(s0)
a = np.zeros((49,49))
a[0,0] = ls.p0(1,0.1)
a[0,1] = -1*ls.q0(1,0.1)
a[48,47] = -1*ls.uI(0.1, 1, ris[48])
a[48,48] = ls.pI(1, 0.1, ris[48])
for i in np.arange(1,48,1):
    a[i, i-1] = -1*ls.uui(1, 0.1, ris[i])
    a[i, i] = ls.ppi(0.1, 1, ris[i])
    a[i,i+1] = -1 * ls.qqi(1, 0.1, ris[i])
print(a)
w = np.linalg.solve(a,s)
print(w)

y1 = [mm.u(step,1, 0.1) for step in ris]
y2 = [el for el in w.flat]

ln0, ln1 = mpl.plot(ris, y1, ris, y2)
mpl.legend((ln0, ln1),('Аналитическое','Численное'))
mpl.grid()
mpl.show()