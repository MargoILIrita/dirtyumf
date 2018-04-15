import multiprocessing
import time

import lilya
import rita
import olya
import numpy as np
import mathmethods as mm
import matplotlib.pyplot as mpl

if __name__ == '__main__':
    print('start')
    stepr = 0.1
    stept = 1
    riarr = [st for st in np.arange(0, 5 - stepr, stepr)]
    #pool = multiprocessing.Pool(processes=3, )
    #array = pool.map(xOy, [(stepr, stept, riarr, 'olya'),(stepr, stept, riarr, 'lilya'),(stepr, stept, riarr, 'rita')])
    #print('finish count new methods' + ' {0:.2f}'.format(time.time()-tt))
    #wolya, wlilya, writa = array[0], array[1], array[2]
    tt = time.time()
    args =(stepr, stept, riarr)
    wlilya = lilya.xOy(args)
    writa = rita.xOy(args)
    wolya = olya.xOy(args)
    y1 = [mm.u(step,1, 0.1) for step in riarr]
    y2 = wlilya[1]
    y3 = [ele for ele in writa[1].flat]
    y4 = wolya[1]
    print('{0}\n{1}\n{2}\n{3}'.format(y1,y2,y3,y4))

    ln0, ln1, ln2, ln3 = mpl.plot(riarr, y1, riarr, y2, riarr, y3, riarr, y4)
    mpl.legend((ln0, ln1, ln2, ln3), ('Аналитическое', 'Численное Лиля', "Численное Рита", 'Численное Оля'),
               title='R: {0}, l: {1}, k: {2}, alf: {3}, c: {4}, betta: {5}, P: {6}, a: {7} \n step for R : {8} \n step '
                     'for T: {9} '.format(mm.da['R'], mm.da['l'], mm.da['k'], mm.da['alf'], mm.da['c'], mm.da['betta'],
                                          mm.da['P'], mm.da['a'], stepr, stept))
    mpl.grid()
    mpl.show()


