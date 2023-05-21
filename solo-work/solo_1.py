def trojkat(bok_a,bok_b,bok_c,h_a):
    pole=1/2*bok_a*h_a
    obwod=bok_a+bok_b+bok_c
    print("Pole wynosi: ",pole,"a obwod: ",obwod)
trojkat(6,8,10,16)

def prostokat(bok_a,bok_b):
    pole=bok_a*bok_b
    obwod=2*(bok_a+bok_b)
    return pole, obwod
print("Pole i obwod wynoszą kolejno: ",prostokat(7,10))

def romb (bok_a,e,f):
    pole=1/2*e*f
    obwod=4*bok_a
    return pole,obwod
print("Pole i obwod wynoszą kolejno: ",romb(5,8,10))