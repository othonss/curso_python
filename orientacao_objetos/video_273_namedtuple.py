from collections import namedtuple

Carta = namedtuple('Carta', ['valor', 'naipe'], defaults=['', ''])
as_espadas = Carta('A', 'Espada')
print(as_espadas)
print(as_espadas.valor)
print(as_espadas.naipe)