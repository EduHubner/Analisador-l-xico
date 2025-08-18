"""

LISTA DE PRODUÇÕES PARA ANÁLISE SINTÁTICA

==========================================
VALIDAÇÃO DE ESCRITA

ESCRITA -> ASPAS PALAVRA ASPAS
PALAVRA -> ID | ID PALAVRA

----------------------------------------
INSTANCIAÇÃO DE VARIÁVEL

INSTANCIAR -> ATRIBUIR | DECLARAR
DECLARAR -> TIPO ID PONTO-VIRGULA
ATRIBUIR -> TIPO ID IGUAL EXPRESSAO PONTO-VIRGULA
TIPO -> INT | FLOAT | STRING | BOOLEAN | CHAR
EXPRESSAO -> VALOR OPERACAO EXPRESSAO | VALOR
OPERACAO -> SOMA | SUBTRACAO | MULTIPLICACAO | DIVISAO
VALOR -> ID | CONSTANTE | ESCRITA

----------------------------------------
ATRIBUIÇÃO DE VALORES

ATRIBUICAO -> ID IGUAL EXPRESSAO PONTO-VIRGULA
EXPRESSAO -> VALOR OPERACAO EXPRESSAO | VALOR (Não precisa instanciar duas vezes)
OPERACAO -> SOMA | SUBTRACAO | MULTIPLICACAO | DIVISAO (Não precisa instanciar duas vezes)
VALOR -> ID | CONSTANTE | ESCRITA (Não precisa instanciar duas vezes)

----------------------------------------



"""

class AnalisadorSintatico:
    def __init__(self, tokens):
        self.cont = 0
        self.lista_tokens = tokens

    def term(self, token):
        result = self.lista_tokens[self.cont] == token
        self.cont += 1
        return result

    def comando(self):
        print("COMANDO -> ATR | DEC")
        anterior = self.cont
        if self.atr():
            return True
        else:
            self.cont = anterior
            return self.dec()

    def atr(self):
        print("ATR -> id atr EXP pv")
        return self.term('id') and self.term('atr') and self.expe() and self.term('pv')

    def expe(self):
        anterior = self.cont
        if self.exp1():
            return True
        else:
            self.cont = anterior
            return self.exp2()

    def exp1(self):
        print("EXP -> id")
        return self.term('id')

    def exp2(self):
        print("EXP -> const")
        return self.term('const')

    def dec(self):
        print("DEC -> tipo id pv")
        return self.term('tipo') and self.term('id') and self.term('pv')

# Exemplo de uso:
lista_tokens = ['id', 'atr', 'id', 'pv']
analisador = AnalisadorSintatico(lista_tokens)

if analisador.comando():
    print("Análise sintática bem-sucedida!")
else:
    print("Erro na análise sintática.")
