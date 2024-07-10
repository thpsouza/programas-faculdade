from matrizes import Matriz, transposta, identidade, zeros
from vetores import Vetor

a = Matriz((0,-1,1,0),2,2)
b = Matriz((4,3,5,1),2,2)
c = Matriz((1,2),2,1)
u = Vetor(0,-1,1,0)
v = Vetor(4,3,5,1)
w = Vetor(7,9)

## Matrizes
print(a+b == b+a)
print(a-b != b-a)
print(a*2 == 2*a)
print(a**2 == Matriz([i**2 for i in a.elementos],2,2))
print(a*b != b*a)
print(transposta(b) == Matriz((4,5,3,1),2,2))
print(identidade(3) == Matriz((1,0,0,0,1,0,0,0,1),3,3))
## Matriz - Vetor coluna
print(a*w == Matriz([-9,7],2,1))
## Matriz coluna - Vetor coluna
M = Matriz(v)
print(v+M == M+v)
print(M-v == v-M)
print(M-v == v-M)
print(v*M == M*v)
## Matriz linha - Matriz linha
print(transposta(u)+transposta(v) == transposta(v)+transposta(u))
print(transposta(u)-transposta(v) != transposta(v)-transposta(u))
print(2*transposta(u) == transposta(u)*2)
print(transposta(v)**2 == Matriz([i**2 for i in transposta(v).elementos],1,4))
## Matriz linha - Vetor coluna
print(transposta(M)*v == 51)
## Vetor coluna - Matriz linha
print(v*transposta(M) == Matriz([16,12,20,4,12,9,15,3,20,15,25,5,4,3,5,1],4,4))
## Vetor coluna - Vetor coluna
print(u+v == v+u)
print(u-v != v-u)
print(2*u == u*2)
print(v**2 == Matriz([i**2 for i in v.elementos],4,1))
print(u*v == v*u)
print(u.produto_diadico(v))
