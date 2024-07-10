from math import log

## Dados:
Th_i = 80 + 273
Th_o = 50 + 273
Tc_i = 15 + 273
mh = 2
cph = 3500
mc = 2.5
U = 2000
cp_agua = 4.18 * 10**3

## Calculando Tc_o
Tc_o = Tc_i + cph*(Th_i - Th_o)*mh / (cp_agua * mc)
print(f"Temperatura de saída da água: Tc,o = {Tc_o}\n")

## Letra a)
# Método da média logarítmica das temperaturas
DT1 = Th_i - Tc_i
DT2 = Th_o - Tc_o

# Calculando área
A = mh*cph*(Th_i - Th_o) * log(DT2/DT1) / (U * (DT2-DT1))
print(f"a)\n Área necessária - correntes paralelas: A = {A}")


## Letra b)
# Método da média logarítmica das temperaturas
DT1 = Th_i - Tc_o
DT2 = Th_o - Tc_i

# Calculando área
A_b = mh*cph*(Th_i - Th_o) * log(DT2/DT1) / (U * (DT2-DT1))
print(f"b)\n Área necessária - correntes contrárias: A = {A_b}")


## Letra c)
P = (Th_o - Th_i) / (Tc_i - Th_i)
R = (Tc_i - Tc_o) / (Th_o - Th_i)
F = 0.94
A = A_b/F
print(f"c)\n R = {R}, P = {P}, F = {F}\n Área necessária - casco e tubo: A = {A}")


## Letra d)
F = 0.95
A = A_b/F 
print(f"d)\n R = {R}, P = {P}, F = {F}\n Área necessária - correntes cruzadas: A = {A}")