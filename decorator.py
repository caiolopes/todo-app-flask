#  import secondfile

#  print('myfile', __name__)


def soma_cinco(func):

    def soma2(numero):
        return func(5, numero)

    return soma2


@soma_cinco
def soma(numero1, numero2):
    return numero1 + numero2


#  soma = soma_cinco(soma)


#  print(soma(5, 5))
print(soma(10))
