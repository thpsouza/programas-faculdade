import sympy as sp
from geral import *

## Dados
Di = 26*10**-3 # m 
De = 30*10**-3 # m
Kaco = 15 # W/mK
Tm = 290 # K
P = 0.135*10**5 # Pascal
m = 0.25 # Kg/s
g = 9.81

## Propriedades água a Tm = 290K:
k = agua.k290
mu = agua.mu290
Pr = agua.Pr290

## Escoamento interno
n = 0.4
Re = 4*m/(pi*Di*mu)
Nu_i = 0.023*Re**(4/5)*Pr**n
h_i = Nu_i*k/Di
print(Re,Nu_i,h_i)

## Propriedades vapor água
hfg = 2378*10**3
pv = 1/11.06

## Propriedades água saturada
Tsat = 325
pl = 1/(1.013) * 10**3
mul = 528*10**-6
kl = 645*10**-3
Cp_l = 4.182*10**3


## Condensação
Tse = sp.Symbol("Tse")
C = 0.729
h_fg = hfg + 0.68*Cp_l*(Tsat-318.929456178806)
Nu_e = C*(pl*g*(pl-pv)*h_fg*De**3/(mul*kl*(Tsat-Tse)))**(1/4)
h_e = Nu_e * kl/De
print(Nu_e,h_e, sep='\n')

## Resistências
Rcond = log(Di/De)/(2*pi*Kaco)
Rconv_i = 1/(pi*Di*h_i)
Rconv_e = 1/(pi*De*h_e)

## Equação para Tse:
f = (Tsat - Tm)/(Rconv_e+Rcond+Rconv_i) - (Tse - Tm)/(Rcond+Rconv_i)
Ts_e = 318.929456178806#sp.solve(f,Tse)[0]

## Fluxo:
q = (Ts_e - Tm)/(Rcond + Rconv_i)

print(Ts_e,q,q/h_fg)
