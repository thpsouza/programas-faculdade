from scipy.special import i0,i1,k0,k1

def eficiencia_aleta_anular(r1,r2c,m):
    '''
    Calcula a eficiência de uma aleta anular
    '''
    C2 = (2*r1/m)/(r2c**2 - r1**2)
    num = k1(m*r1)*i1(m*r2c) - i1(m*r1)*k1(m*r2c)
    den = i0(m*r1)*k1(m*r2c) + k0(m*r1)*i1(m*r2c)
    return C2*num/den

def eficiencia_aleta_uniforme(qa,h,thetab,Aa):
    '''
    Calcula a eficiência de uma aleta uniforme
    '''
    return qa/(h*Aa*thetab)

