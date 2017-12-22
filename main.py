import UIforR as Ri
import UI as T
import  mathmethods


da = mathmethods.getparams()
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
    da['a'] = float(R)/5

ec = int(input("Введите точность (целое число - количество знаков после запятой) "))
print("Подождите, пожалуйста, выполняются вычисления...")


Ri.drawUIR(da,ec)
T.drawUIT(da, ec)