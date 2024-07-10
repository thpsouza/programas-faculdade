from perda_de_carga import PerdaDeCarga
from fator_de_atrito import colebrook_white
from adimensionais import reynolds

L = 24.4
D = 0.013
v = 3.2
p = 999 
m = 1.002*10**-3
Re = reynolds(p,v,D,m,True)
E_D = 0.046*10**-3/0.013
print(E_D)

def main():
    perda_de_carga = PerdaDeCarga(L,D,v,Fd=0.028)
    hp = perda_de_carga.localizada()
    print(hp)

if __name__ == "__main__":
    main()