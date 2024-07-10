def R(unidade='J/(mol*K)'):
    '''
    Retorna o valor da constante universal dos gases em 3 unidades possíveis:

    >>> R('J/(mol*K)') 
    8.315

    >>> R('atm*L/(mol*K)') 
    0.082

    >>> R('J/(mol*K)') 
    62.3
    '''
    valores = {
        'J/mol*K':8.315,
        'J/(mol*K)':8.315,

        'atm*L/mol*K':0.082,  
        'atm*L/(mol*K)':0.082,  
        '(atm*L)/(mol*K)':0.082, 

        'mmHg*L/mol*K':62.3,
        'mmHg*L/(mol*K)':62.3,
        '(mmHg*L)/(mol*K)':62.3
    }
    return valores[unidade]


def F():
    '''
    Constante de Faraday em Coulomb/mol 
    '''
    return 96485






