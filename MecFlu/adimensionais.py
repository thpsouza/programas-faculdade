def reynolds(p,v,D,m,imprimir=False):
    '''
    Retorna o número de Reynolds
    
    - p:    massa específica (densidade)
    - v:    velocidade do escoamento
    - D:    comprimento específico (diâmetro do tubo) 
    - m:    viscosidade dinâmica

    float, float, float, float --> float
    '''
    Re = p*v*D/m
    if imprimir:
        print(Re)
    return Re