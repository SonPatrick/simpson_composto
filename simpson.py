def func(x):
    from math import sqrt, exp, sin
    #f = 1/x
    f = exp(x)
    #f = pow(x,4)
    #f = 1/(x+1)
    #f = sqrt(1+pow(x,2))
    #f = sin(x)
    return f

def simpson(a, b, n):
    h = (b-a)/n
    x = []
    pm = a+h
    x.append(round(pm, 1))
    x_impar = []
    x_par = []
    soma_par = 0
    soma_impar = 0
    result = 0
    count = 0
    for i in range(1, n-1, 1):
        x.append(x[i-1]+h)
    for i in range(0, n-1, 2):
        x_impar.append(x[i])
        soma_impar += func(x_impar[count])
        count += 1
    count = 0
    for i in range(1, n-1, 2):
        x_par.append(x[i])
        soma_par += func(x_par[count])
        count += 1
    result = (h/3)*(func(a)+2*(soma_par)+4*(soma_impar)+func(b))
    #print('lista =',x)
    #print('lista impar =', x_impar)
    #print('lista_par =', x_par)
    print('resultado =', result)
simpson(0, 2, 1000)