import json
#Tive que pesquisar como fazer para salvar no mesmo diretório que está meu arquivo atual, a solução encontrada foi o pathlib
from pathlib import Path

CAMINHO_ARQUIVO = Path(__file__).parent / 'aula209.json'

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

p1 = Pessoa('Othon', 30)
p2 = Pessoa('Sabrina', 31)
p3 = Pessoa('Ana', 10)

#Nesse contexto, vars() e .__dict__ são equivalentes por desempenharem as mesmas funções
bd = [vars(p1), p2.__dict__, vars(p3)]

def fazer_dump():
    with open(CAMINHO_ARQUIVO, 'w', encoding='utf-8') as arquivo:
        json.dump(bd, arquivo, ensure_ascii=False, indent=2)

if __name__ == '__main__':
    fazer_dump()