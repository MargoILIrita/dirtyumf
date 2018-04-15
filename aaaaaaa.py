import multiprocessing

import lilya
import rita
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
    a[0,1] = ls.q0(ht,hr)
    a[len-1,len-2] = ls.uI(hr, ht, ris[len-1])
    a[len-1,len-1] = ls.pI(ht, hr, ris[len-1])
    for i in np.arange(1,len-1,1):
        a[i, i-1] = ls.uui(ht, hr, ris[i])
        a[i, i] = ls.ppi(hr, ht, ris[i])
        a[i,i+1] = ls.qqi(ht, hr, ris[i])
    return np.linalg.solve(a,s)

def xOy(args):
    stepr, stept, riarr, name = args[0], args[1], args[2], args[3]
    res = [np.zeros((riarr.__len__(), 1)), ]
    for k in range(1, 100, stept):
        if name == 'olya':
            res.append(olya.all(res[k - 1], stept, stepr, riarr))
        elif name == 'lilya':
            res.append(findW(res[k - 1], stept, stepr, riarr, lilya))
        else: res.append(findW(res[k - 1], stept, stepr, riarr, rita))
    return res

if __name__ == '__main__':
    print('start')
    stepr = 0.1
    stept = 1
    riarr = [st for st in np.arange(0, 5 - stepr, stepr)]
    pool = multiprocessing.Pool(processes=3, )
    array = pool.map(xOy, [(stepr, stept, riarr, 'olya'),(stepr, stept, riarr, 'lilya'),(stepr, stept, riarr, 'rita')])
    print('finish count new methods')
    wolya, wlilya, writa = array[0], array[1], array[2]

    y1 = [mm.u(step,1, 0.1) for step in riarr]
    y2 = [el for el in wlilya[1].flat]
    y3 = [ele for ele in writa[1].flat]
    y4 = wolya[1]
    print('{0}\n{1}\n{2}\n{3}'.format(y1,y2,y3,y4))

    ln0, ln1, ln2, ln3 = mpl.plot(riarr, y1, riarr, y2, riarr, y3, riarr, y4)
    mpl.legend((ln0, ln1, ln2, ln3), ('Аналитическое', 'Численное Лиля', "Численное Рита", 'Численное Оля'))
    mpl.grid()
    mpl.show()


