import math
#trojkat
a=10
b=12
c=8
h=6

pole=1/2*(a*h)
print(pole)
obwod=a+b+c 
print("Pole trojkata wynosi " +str(pole) + " a obwod " +str(obwod))

#trapez
a_tr=15
b_tr=4
c_tr=3
d_tr=4
h_tr=10
pole_trapez=1/2*(a_tr+b_tr)*h_tr
obw_trapez=a_tr+b_tr+c_tr+d_tr
print("Pole trapezu wynosi " + str(pole_trapez) + " a obwod wynosi " + str(obw_trapez))

#romb
a_ro=10
e_ro=16
f_ro=12
obw_romb=4*a_ro
pole_romb=1/2*e_ro*f_ro
print("Pole rombu wynosi" + str(pole_romb) + " a obwod " +str(obw_romb))

#kolo
r=10
obwod_kol = 2*math.pi*r
pole_kol=math.pi*math.pow(r,2)
print("Pole kola wynosi " + str(pole_kol) + " a obwod " +str(obwod_kol))

#prostokat
a_pr=10
b_pr=15
obw_pr=2*(a_pr+b_pr)
pole_pr=a_pr*b_pr
print("Pole prostokata wynosi" + str(pole_pr) + " a obwod wynosi " +str(obw_pr))


