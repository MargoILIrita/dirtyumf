import lilya
import  rita
import olya
import numpy as np
import mathmethods as mm
import matplotlib.pyplot as mpl

def findW(w, ht, hr, ris, ls):
    len = ris.__len__()
    s0 = []
    j = 0
    for ri in ris:
        if (ri == 0):
            s0.append([ls.s0(0, ht),])
        else:
            s0.append([ls.ssi(w[j],ri, ht),])
        j+=1
    s = np.matrix(s0)
    a = np.zeros((len,len))
    a[0,0] = ls.p0(ht,hr)
    a[0,1] = -1*ls.q0(ht,hr)
    a[len-1,len-2] = -1*ls.uI(hr, ht, ris[len-1])
    a[len-1,len-1] = ls.pI(ht, hr, ris[len-1])
    for i in np.arange(1,len-1,1):
        a[i, i-1] = -1*ls.uui(ht, hr, ris[i])
        a[i, i] = ls.ppi(hr, ht, ris[i])
        a[i,i+1] = -1 * ls.qqi(ht, hr, ris[i])
    return np.linalg.solve(a,s)

radius = 5
stepr = 0.1
stept = 1
riarr = [st for st in np.arange(0,radius-stepr,stepr)]
wlilya = [np.zeros((riarr.__len__(), 1)), ]
writa = [np.zeros((riarr.__len__(), 1)), ]
wolya = [np.zeros((riarr.__len__(), 1)), ]
for k in range(1,100,stept):
    wlilya.append(findW(wlilya[k - 1], stept, stepr, riarr, lilya))
    writa.append(findW(writa[k - 1], stept, stepr, riarr, rita))
    wolya.append(olya.all(wolya[k-1],stept, stepr, riarr))
y1 = [mm.u(step,1, 0.1) for step in riarr]
y2 = [el for el in wlilya[1].flat]
y3 = [ele for ele in writa[1].flat]
y4 = wolya[1]

ln0 ,ln1, ln2, ln3 = mpl.plot(riarr, y1, riarr, y2, riarr, y3, riarr, y4)
mpl.legend((ln0,ln1, ln2, ln3),('Аналитическое','Численное Лиля', "Численное Рита", 'Численное Оли'))
mpl.grid()
mpl.show()