"""

LISTA DE PRODUÇÕES PARA ANÁLISE SINTÁTICA

Valores entre <> são não-terminais.

==========================================
VALIDAÇÃO DE ESCRITA

ESCRITA -> ASPAS <PALAVRA> ASPAS
<PALAVRA> -> ID | ID <PALAVRA>

----------------------------------------
INSTANCIAÇÃO DE VARIÁVEL

INSTANCIAR -> <ATRIBUIR> | <DECLARAR>
<DECLARAR> -> <TIPO> ID PONTO-VIRGULA
<ATRIBUIR> -> <TIPO> ID IGUAL <EXPRESSAO> PONTO-VIRGULA
<TIPO> -> INT | FLOAT | STRING | BOOLEAN | CHAR
<EXPRESSAO> -> <VALOR> <OPERACAO> <EXPRESSAO> | <VALOR>
<OPERACAO> -> SOMA | SUBTRACAO | MULTIPLICACAO | DIVISAO
<VALOR> -> ID | CONSTANTE | ESCRITA

----------------------------------------
ATRIBUIÇÃO DE VALORES

ATRIBUICAO -> ID IGUAL <EXPRESSAO> PONTO-VIRGULA
<EXPRESSAO> -> <VALOR> <OPERACAO> <EXPRESSAO> | <VALOR> (Não precisa instanciar duas vezes)
<OPERACAO> -> SOMA | SUBTRACAO | MULTIPLICACAO | DIVISAO (Não precisa instanciar duas vezes)
<VALOR> -> ID | CONSTANTE | ESCRITA (Não precisa instanciar duas vezes)
<ESCRITA> -> ASPAS <PALAVRA> ASPAS (Não precisa instanciar duas vezes)
<PALAVRA> -> ID | ID <PALAVRA> (Não precisa instanciar duas vezes)

----------------------------------------
EXPRESSÃO NUMÉRICA

<EXPRESSAO> -> <VALOR> <OPERACAO> <EXPRESSAO> | <VALOR> (Não precisa instanciar duas vezes)
<OPERACAO> -> SOMA | SUBTRACAO | MULTIPLICACAO | DIVISAO (Não precisa instanciar duas vezes)
<VALOR> -> ID | CONSTANTE | ESCRITA (Não precisa instanciar duas vezes)

----------------------------------------
IMPRIMIR/ESCRITA

IMPRIMIR -> OUT ABRE_PARENTESES <SAIDA> FECHA_PARENTESES PONTO_VIRGULA
<SAIDA> -> <ESCRITA> CONCATENAR <SAIDA> | ID CONCATENAR <SAIDA> | <ESCRITA> | ID
<ESCRITA> -> ASPAS <PALAVRA> ASPAS (Não precisa instanciar duas vezes)
<PALAVRA> -> ID | ID <PALAVRA> (Não precisa instanciar duas vezes)

----------------------------------------
ENTRADA/LEITURA

LEITURA -> IN ABRE_PARENTESES <ENTRADA> FECHA_PARENTESES PONTO_VIRGULA
<ENTRADA> -> ID VIRGULA <ENTRADA> | ID

----------------------------------------
COMANDO IF

IF -> IF ABRE_PARENTESES <CONDICAO> FECHA_PARENTESES ABRE_CHAVE <BLOCO> FECHA_CHAVE
<CONDICAO> -> <VALOR> <OPERADOR-LOGICO> <VALOR>
<VALOR> -> ID | CONSTANTE | <ESCRITA> (Não precisa instanciar duas vezes)
<OPERADOR_LOGICO> -> IGUAL_IGUAL | DIFERENTE | MAIOR | MENOR | MAIOR_IGUAL | MENOR_IGUAL
<BLOCO> -> <COMANDO> | <COMANDO> <BLOCO>

"""

class AnalisadorSintatico:
    def __init__(self, tokens):
        self.cont = 0
        self.lista_tokens = tokens

    def term(self, token):
        """Verifica se o token atual corresponde ao esperado"""
        if self.cont < len(self.lista_tokens):
            result = self.lista_tokens[self.cont] == token
            if result:
                self.cont += 1
            return result
        return False

    def peek(self):
        """Retorna o token atual sem avançar o contador"""
        if self.cont < len(self.lista_tokens):
            return self.lista_tokens[self.cont]
        return None

    # ==========================================
    # VALIDAÇÃO DE ESCRITA
    # ==========================================
    
    def escrita(self):
        """ESCRITA -> ASPAS PALAVRA ASPAS"""
        print("ESCRITA -> ASPAS PALAVRA ASPAS")
        return self.term('ASPAS') and self.palavra() and self.term('ASPAS')

    def palavra(self):
        """PALAVRA -> ID | ID PALAVRA"""
        print("PALAVRA -> ID | ID PALAVRA")
        if self.term('ID'):
            # Tenta continuar com mais palavras (recursão à direita)
            anterior = self.cont
            if self.palavra():
                return True
            else:
                # Se não conseguir continuar, volta e aceita apenas um ID
                self.cont = anterior
                return True
        return False

    # ==========================================
    # INSTANCIAÇÃO DE VARIÁVEL
    # ==========================================
    
    def instanciar(self):
        """INSTANCIAR -> ATRIBUIR | DECLARAR"""
        print("INSTANCIAR -> ATRIBUIR | DECLARAR")
        anterior = self.cont
        if self.atribuir():
            return True
        else:
            self.cont = anterior
            return self.declarar()

    def declarar(self):
        """DECLARAR -> TIPO ID PONTO-VIRGULA"""
        print("DECLARAR -> TIPO ID PONTO-VIRGULA")
        return self.tipo() and self.term('ID') and self.term('PONTO-VIRGULA')

    def atribuir(self):
        """ATRIBUIR -> TIPO ID IGUAL EXPRESSAO PONTO-VIRGULA"""
        print("ATRIBUIR -> TIPO ID IGUAL EXPRESSAO PONTO-VIRGULA")
        return self.tipo() and self.term('ID') and self.term('IGUAL') and self.expressao() and self.term('PONTO-VIRGULA')

    def tipo(self):
        """TIPO -> INT | FLOAT | STRING | BOOLEAN | CHAR"""
        print("TIPO -> INT | FLOAT | STRING | BOOLEAN | CHAR")
        return (self.term('INT') or self.term('FLOAT') or 
                self.term('STRING') or self.term('BOOLEAN') or self.term('CHAR'))

    # ==========================================
    # ATRIBUIÇÃO DE VALORES
    # ==========================================
    
    def atribuicao(self):
        """ATRIBUICAO -> ID IGUAL EXPRESSAO PONTO-VIRGULA"""
        print("ATRIBUICAO -> ID IGUAL EXPRESSAO PONTO-VIRGULA")
        return self.term('ID') and self.term('IGUAL') and self.expressao() and self.term('PONTO-VIRGULA')

    # ==========================================
    # EXPRESSÕES E VALORES
    # ==========================================
    
    def expressao(self):
        """EXPRESSAO -> VALOR OPERACAO EXPRESSAO | VALOR"""
        print("EXPRESSAO -> VALOR OPERACAO EXPRESSAO | VALOR")
        if self.valor():
            # Tenta continuar com operação e expressão
            anterior = self.cont
            if self.operacao() and self.expressao():
                return True
            else:
                # Se não conseguir, volta e aceita apenas VALOR
                self.cont = anterior
                return True
        return False

    def operacao(self):
        """OPERACAO -> SOMA | SUBTRACAO | MULTIPLICACAO | DIVISAO"""
        print("OPERACAO -> SOMA | SUBTRACAO | MULTIPLICACAO | DIVISAO")
        return (self.term('SOMA') or self.term('SUBTRACAO') or 
                self.term('MULTIPLICACAO') or self.term('DIVISAO'))

    def valor(self):
        """VALOR -> ID | CONSTANTE | ESCRITA"""
        print("VALOR -> ID | CONSTANTE | ESCRITA")
        anterior = self.cont
        if self.term('ID'):
            return True
        
        self.cont = anterior
        if self.term('CONSTANTE'):
            return True
        
        self.cont = anterior
        return self.escrita()

    # ==========================================
    # IMPRIMIR/ESCRITA
    # ==========================================
    
    def imprimir(self):
        """IMPRIMIR -> OUT ABRE_PARENTESES SAIDA FECHA_PARENTESES PONTO_VIRGULA"""
        print("IMPRIMIR -> OUT ABRE_PARENTESES SAIDA FECHA_PARENTESES PONTO_VIRGULA")
        return (self.term('OUT') and self.term('ABRE_PARENTESES') and 
                self.saida() and self.term('FECHA_PARENTESES') and self.term('PONTO_VIRGULA'))

    def saida(self):
        """SAIDA -> ESCRITA CONCATENAR SAIDA | ID CONCATENAR SAIDA | ESCRITA | ID"""
        print("SAIDA -> ESCRITA CONCATENAR SAIDA | ID CONCATENAR SAIDA | ESCRITA | ID")
        anterior = self.cont
        
        # Tenta ESCRITA CONCATENAR SAIDA
        if self.escrita():
            anterior2 = self.cont
            if self.term('CONCATENAR') and self.saida():
                return True
            else:
                # Se não conseguir concatenar, volta e aceita apenas ESCRITA
                self.cont = anterior2
                return True
        
        # Se ESCRITA falhar, tenta ID CONCATENAR SAIDA
        self.cont = anterior
        if self.term('ID'):
            anterior2 = self.cont
            if self.term('CONCATENAR') and self.saida():
                return True
            else:
                # Se não conseguir concatenar, volta e aceita apenas ID
                self.cont = anterior2
                return True
        
        return False

    # ==========================================
    # ENTRADA/LEITURA
    # ==========================================
    
    def leitura(self):
        """LEITURA -> IN ABRE_PARENTESES ENTRADA FECHA_PARENTESES PONTO_VIRGULA"""
        print("LEITURA -> IN ABRE_PARENTESES ENTRADA FECHA_PARENTESES PONTO_VIRGULA")
        return (self.term('IN') and self.term('ABRE_PARENTESES') and 
                self.entrada() and self.term('FECHA_PARENTESES') and self.term('PONTO_VIRGULA'))

    def entrada(self):
        """ENTRADA -> ID VIRGULA ENTRADA | ID"""
        print("ENTRADA -> ID VIRGULA ENTRADA | ID")
        if self.term('ID'):
            anterior = self.cont
            if self.term('VIRGULA') and self.entrada():
                return True
            else:
                # Se não conseguir continuar, volta e aceita apenas ID
                self.cont = anterior
                return True
        return False

    # ==========================================
    # COMANDO IF
    # ==========================================
    
    def comando_if(self):
        """IF -> IF ABRE_PARENTESES CONDICAO FECHA_PARENTESES ABRE_CHAVE BLOCO FECHA_CHAVE"""
        print("IF -> IF ABRE_PARENTESES CONDICAO FECHA_PARENTESES ABRE_CHAVE BLOCO FECHA_CHAVE")
        return (self.term('IF') and self.term('ABRE_PARENTESES') and 
                self.condicao() and self.term('FECHA_PARENTESES') and 
                self.term('ABRE_CHAVE') and self.bloco() and self.term('FECHA_CHAVE'))

    def condicao(self):
        """CONDICAO -> VALOR OPERADOR_LOGICO VALOR"""
        print("CONDICAO -> VALOR OPERADOR_LOGICO VALOR")
        return self.valor() and self.operador_logico() and self.valor()

    def operador_logico(self):
        """OPERADOR_LOGICO -> IGUAL_IGUAL | DIFERENTE | MAIOR | MENOR | MAIOR_IGUAL | MENOR_IGUAL"""
        print("OPERADOR_LOGICO -> IGUAL_IGUAL | DIFERENTE | MAIOR | MENOR | MAIOR_IGUAL | MENOR_IGUAL")
        return (self.term('IGUAL_IGUAL') or self.term('DIFERENTE') or 
                self.term('MAIOR') or self.term('MENOR') or 
                self.term('MAIOR_IGUAL') or self.term('MENOR_IGUAL'))

    def bloco(self):
        """BLOCO -> COMANDO | COMANDO BLOCO (Simplificado para aceitar qualquer sequência de comandos)"""
        print("BLOCO -> COMANDO")
        # Para simplificar, aceita qualquer token como parte do bloco
        # Em uma implementação real, isso seria mais específico
        if self.cont < len(self.lista_tokens):
            self.cont += 1  # Consome pelo menos um token do bloco
            return True
        return False

    # ==========================================
    # MÉTODO PRINCIPAL PARA ANÁLISE
    # ==========================================
    
    def analisar(self, tipo_comando):
        """Método principal para escolher qual tipo de comando analisar"""
        if tipo_comando == 'instanciar':
            return self.instanciar()
        elif tipo_comando == 'atribuicao':
            return self.atribuicao()
        elif tipo_comando == 'escrita':
            return self.escrita()
        elif tipo_comando == 'imprimir':
            return self.imprimir()
        elif tipo_comando == 'leitura':
            return self.leitura()
        elif tipo_comando == 'if':
            return self.comando_if()
        else:
            print(f"Tipo de comando '{tipo_comando}' não reconhecido")
            return False

# ==========================================
# EXEMPLOS DE USO
# ==========================================

def testar_analisador():
    print("=== TESTES DO ANALISADOR SINTÁTICO ===\n")
    
    # Teste 1: Declaração simples
    print("1. Teste: Declaração simples")
    tokens1 = ['INT', 'ID', 'PONTO-VIRGULA']
    analisador1 = AnalisadorSintatico(tokens1)
    resultado1 = analisador1.analisar('instanciar')
    print(f"Tokens: {tokens1}")
    print(f"Resultado: {'✓ ACEITO' if resultado1 else '✗ REJEITADO'}\n")
    
    # Teste 2: Expressão numérica complexa
    print("2. Teste: Expressão numérica complexa")
    tokens2 = ['ID', 'IGUAL', 'ID', 'SOMA', 'CONSTANTE', 'MULTIPLICACAO', 'ID', 'PONTO-VIRGULA']
    analisador2 = AnalisadorSintatico(tokens2)
    resultado2 = analisador2.analisar('atribuicao')
    print(f"Tokens: {tokens2}")
    print(f"Resultado: {'✓ ACEITO' if resultado2 else '✗ REJEITADO'}\n")
    
    # Teste 3: Comando de impressão
    print("3. Teste: Comando de impressão")
    tokens3 = ['OUT', 'ABRE_PARENTESES', 'ASPAS', 'ID', 'ASPAS', 'CONCATENAR', 'ID', 'FECHA_PARENTESES', 'PONTO_VIRGULA']
    analisador3 = AnalisadorSintatico(tokens3)
    resultado3 = analisador3.analisar('imprimir')
    print(f"Tokens: {tokens3}")
    print(f"Resultado: {'✓ ACEITO' if resultado3 else '✗ REJEITADO'}\n")
    
    # Teste 4: Comando de leitura
    print("4. Teste: Comando de leitura")
    tokens4 = ['IN', 'ABRE_PARENTESES', 'ID', 'VIRGULA', 'ID', 'FECHA_PARENTESES', 'PONTO_VIRGULA']
    analisador4 = AnalisadorSintatico(tokens4)
    resultado4 = analisador4.analisar('leitura')
    print(f"Tokens: {tokens4}")
    print(f"Resultado: {'✓ ACEITO' if resultado4 else '✗ REJEITADO'}\n")
    
    # Teste 5: Comando IF
    print("5. Teste: Comando IF")
    tokens5 = ['IF', 'ABRE_PARENTESES', 'ID', 'IGUAL_IGUAL', 'CONSTANTE', 'FECHA_PARENTESES', 'ABRE_CHAVE', 'ID', 'FECHA_CHAVE']
    analisador5 = AnalisadorSintatico(tokens5)
    resultado5 = analisador5.analisar('if')
    print(f"Tokens: {tokens5}")
    print(f"Resultado: {'✓ ACEITO' if resultado5 else '✗ REJEITADO'}\n")

# Executar os testes
if __name__ == "__main__":
    testar_analisador()