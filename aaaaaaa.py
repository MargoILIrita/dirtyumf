import multiprocessing
import time

import lilya
import rita
import olya
import numpy as np
import mathmethods as mm
import matplotlib.pyplot as mpl

if __name__ == '__main__':
    da = mm.getparams()
    print("Текущие параметры")
    print("R = {0}  l = {1}  k = {2}".format(da['R'], da['l'], da['k']))
    print("alfa = {0} c = {1} betta = {2}".format(da['alf'], da['c'], da['betta']))
    print("P = {0}, a = {1}".format(da['P'], da['a']))

    yes = input("Введите Yes, если хотите изменить параметры ")
    if yes.upper() == "YES":
        R = input("Введите R ")
        l = input("Введите l ")
        k = input("Введите k ")
        alfa = input("Введите alfa ")
        c = input("Введите c ")
        betta = input("Введите betta ")
        P = input("Введите P ")
        da['R'] = float(R)
        da['l'] = float(l)
        da['k'] = float(k)
        da['alf'] = float(alfa)
        da['c'] = float(c)
        da['betta'] = float(betta)
        da['P'] = float(P)
        da['a'] = float(R) / 5

    stepr = 5/int(input("Введите количество шагов по R "))
    stept = int(100/int(input('и по T ')))
    curtime = int(input("Введите момент времени "))
    print("Подождите, пожалуйста, выполняются вычисления...")
    riarr = [st for st in np.arange(0, 5 , stepr)]
    #pool = multiprocessing.Pool(processes=3, )
    #array = pool.map(xOy, [(stepr, stept, riarr, 'olya'),(stepr, stept, riarr, 'lilya'),(stepr, stept, riarr, 'rita')])
    #print('finish count new methods' + ' {0:.2f}'.format(time.time()-tt))
    #wolya, wlilya, writa = array[0], array[1], array[2]
    tt = time.time()
    args =(stepr, stept, riarr)
    wlilya = lilya.xOy(args)
    writa = rita.xOy(args)
    wolya = olya.xOy(args)
    y1 = [mm.u(step,curtime, 0.1) for step in riarr]
    y2 = wlilya[curtime]
    y3 = [ele for ele in writa[curtime].flat]
    y4 = wolya[curtime]
    #print('{0}\n{1}\n{2}\n{3}'.format(y1,y2,y3,y4))

    ln0, ln1, ln2 = mpl.plot(riarr, y1, riarr, y2, riarr, y3)
    mpl.legend((ln0, ln1, ln2), ('Аналитическое', 'Численное Лиля', "Численное Рита"),
               title='R: {0}, l: {1}, k: {2}, alf: {3}, c: {4}, betta: {5}, P: {6}, a: {7} \n step for R : {8} \n step '
                     'for T: {9} \n time = {10}'.format(mm.da['R'], mm.da['l'], mm.da['k'], mm.da['alf'], mm.da['c'], mm.da['betta'],
                                          mm.da['P'], mm.da['a'], stepr, stept, curtime))
    mpl.grid()
    mpl.show()

#make some dirty shit

