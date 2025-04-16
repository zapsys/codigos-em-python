# Função que gera strings com 20 caracteres
# (com letras e números) de forma aleatória
import random
import string


def key_generator(
    size=20,
    chars=string.ascii_letters
    + string.digits
):
    return ''.join(random.choice(chars) for _ in range(size))


print(key_generator())
