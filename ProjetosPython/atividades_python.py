def soma_até_n(n,soma=0):
    """
    Esta função soma os números até um certo numero (n),
    utilizando recursão.
    """
    if n == 0:
        return 0 
    elif n == 1:
        soma += n
        return soma    
    else:
        soma += n
        return soma_até_n(n - 1, soma)
#print(soma_até_n(100))


def potencia(x,n,r=1):
    """
    Esta função utiliza de estruturas de repetição para
    gerar a potencia do primeiro numero (x) elevado ao segundo (n).
    Utiliza-se a variavel (r) para armazenar o resultado de cada operação durante o loop.
    """

    for i in range(n):
        r *= x
        return potencia(x,n-1,r)
    return r

print(potencia(2,3), 2**8)
