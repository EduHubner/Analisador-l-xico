"""

LISTA DE PRODUÇÕES PARA ANÁLISE SINTÁTICA

Valores entre <> são não-terminais.

==========================================
VALIDAÇÃO DE ESCRITA

<ESCRITA> -> ASPAS <PALAVRA> ASPAS
<PALAVRA> -> ID | ID <PALAVRA>

----------------------------------------
INSTANCIAÇÃO DE VARIÁVEL

<INSTANCIAR> -> <ATRIBUIR> | <DECLARAR>
<DECLARAR> -> <TIPO> ID PONTO-VIRGULA
<ATRIBUIR> -> <TIPO> ID IGUAL <EXPRESSAO> PONTO-VIRGULA
<TIPO> -> INT | FLOAT | STRING | BOOLEAN | CHAR
<EXPRESSAO> -> <VALOR> <OPERACAO> <EXPRESSAO> | <VALOR>
<OPERACAO> -> SOMA | SUBTRACAO | MULTIPLICACAO | DIVISAO
<VALOR> -> ID | CONSTANTE | <ESCRITA>
<ESCRITA> -> ASPAS <PALAVRA> ASPAS (Não precisa instanciar duas vezes)
<PALAVRA> -> ID | ID <PALAVRA> (Não precisa instanciar duas vezes)

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
<BLOCO> -> COMANDO PONTO_VIRGULA

----------------------------------------
DECLARAÇÃO DE FUNÇÃO

FUNCAO -> FUN ABRE_PARENTESES <PARAMETROS> FECHA_PARENTESES ABRE_CHAVE <BLOCO> FECHA_CHAVE
<PARAMETROS> -> <TIPO> ID VIRGULA <PARAMETROS> | <TIPO> ID | VAZIO
<TIPO> -> INT | FLOAT | STRING | BOOLEAN | CHAR
<BLOCO> -> COMANDO PONTO_VIRGULA

----------------------------------------
CHAMADA DE FUNÇÃO

CHAMADA_FUNCAO -> PONTO_ACESSO ID ABRE_PARENTESES <ARGUMENTOS> FECHA_PARENTESES PONTO_VIRGULA
<ARGUMENTOS> -> <VALOR> VIRGULA <ARGUMENTOS> | <VALOR> | VAZIO
<VALOR> -> ID | CONSTANTE | <ESCRITA> (Não precisa instanciar duas vezes)
<ESCRITA> -> ASPAS <PALAVRA> ASPAS (Não precisa instanciar duas vezes)
<PALAVRA> -> ID | ID <PALAVRA> (Não precisa instanciar duas vezes)

----------------------------------------
COMANDO FOR

FOR -> FOR ABRE_PARENTESES <ATRIBUICAO_FOR> PONTO_VIRGULA <CONDICAO> PONTO_VIRGULA <PASSO> FECHA_PARENTESES ABRE_CHAVE <BLOCO> FECHA_CHAVE
<ATRIBUICAO_FOR> -> ID IGUAL <VALOR> | VAZIO
<VALOR> -> ID | CONSTANTE | <ESCRITA> (Não precisa instanciar duas vezes)
<ESCRITA> -> ASPAS <PALAVRA> ASPAS (Não precisa instanciar duas vezes)
<PALAVRA> -> ID | ID <PALAVRA> (Não precisa instanciar duas vezes)
<CONDICAO_FOR> -> ID <OPERADOR-LOGICO> <VALOR> | VAZIO
<OPERADOR_LOGICO> -> IGUAL_IGUAL | DIFERENTE | MAIOR | MENOR | MAIOR_IGUAL | MENOR_IGUAL (Não precisa instanciar duas vezes)
<PASSO> -> ID INCREMENTO | ID DECREMENTO | ID IGUAL <EXPRESSAO> | VAZIO
<EXPRESSAO> -> <VALOR> <OPERACAO> <EXPRESSAO> | <VALOR> (Não precisa instanciar duas vezes)
<OPERACAO> -> SOMA | SUBTRACAO | MULTIPLICACAO | DIVISAO (Não precisa instanciar duas vezes)
<BLOCO> -> COMANDO PONTO_VIRGULA

----------------------------------------
COMANDO WHILE

WHILE -> WHILE ABRE_PARENTESES <CONDICAO> FECHA_PARENTESES ABRE_CHAVE <BLOCO> FECHA_CHAVE
<CONDICAO> -> <VALOR> <OPERADOR-LOGICO> <VALOR> (Não precisa instanciar duas vezes)
<VALOR> -> ID | CONSTANTE | <ESCRITA> (Não precisa instanciar duas vezes)
<OPERADOR_LOGICO> -> IGUAL_IGUAL | DIFERENTE | MAIOR | MENOR | MAIOR_IGUAL | MENOR_IGUAL (Não precisa instanciar duas vezes)
<BLOCO> -> COMANDO PONTO_VIRGULA
<ESCRITA> -> ASPAS <PALAVRA> ASPAS (Não precisa instanciar duas vezes)
<PALAVRA> -> ID | ID <PALAVRA> (Não precisa instanciar duas vezes)

"""
from lexico import Lexico
from token import Token

class AnalisadorSLR:
    def __init__(self):
        # Gramática estendida com novas produções
        self.gramatica = {
            0: ("S'", ["PROGRAMA"]),
            1: ("PROGRAMA", ["DECLARAR"]),
            2: ("PROGRAMA", ["ATRIBUIR"]), 
            3: ("PROGRAMA", ["ATRIBUICAO"]),
            4: ("PROGRAMA", ["IMPRIMIR"]),
            5: ("PROGRAMA", ["LEITURA"]),
            6: ("PROGRAMA", ["COMANDO_IF"]),
            7: ("PROGRAMA", ["FUNCAO"]),
            8: ("PROGRAMA", ["CHAMADA_FUNCAO"]),
            9: ("PROGRAMA", ["FOR"]),
            10: ("PROGRAMA", ["WHILE"]),
            
            # Produções originais
            11: ("DECLARAR", ["TIPO", "ID", "PONTO_VIRGULA"]),
            12: ("ATRIBUIR", ["TIPO", "ID", "IGUAL", "EXPRESSAO", "PONTO_VIRGULA"]),
            13: ("ATRIBUICAO", ["ID", "IGUAL", "EXPRESSAO", "PONTO_VIRGULA"]),
            14: ("EXPRESSAO", ["VALOR", "OPERACAO", "EXPRESSAO"]),
            15: ("EXPRESSAO", ["VALOR"]),
            16: ("TIPO", ["INT"]),
            17: ("TIPO", ["FLOAT"]),
            18: ("TIPO", ["STRING"]),
            19: ("TIPO", ["BOOLEAN"]),
            20: ("TIPO", ["CHAR"]),
            21: ("OPERACAO", ["SOMA"]),
            22: ("OPERACAO", ["SUBTRACAO"]),
            23: ("OPERACAO", ["MULTIPLICACAO"]),
            24: ("OPERACAO", ["DIVISAO"]),
            25: ("VALOR", ["ID"]),
            26: ("VALOR", ["CONSTANTE"]),
            27: ("VALOR", ["ESCRITA"]),
            28: ("ESCRITA", ["ASPAS", "PALAVRA", "ASPAS"]),
            29: ("PALAVRA", ["ID"]),
            30: ("PALAVRA", ["ID", "PALAVRA"]),
            31: ("IMPRIMIR", ["OUT", "ABRE_PARENTESES", "SAIDA", "FECHA_PARENTESES", "PONTO_VIRGULA"]),
            32: ("SAIDA", ["ID"]),
            33: ("LEITURA", ["IN", "ABRE_PARENTESES", "ENTRADA", "FECHA_PARENTESES", "PONTO_VIRGULA"]),
            34: ("ENTRADA", ["ID"]),
            
            # Novas produções - COMANDO IF
            35: ("COMANDO_IF", ["IF", "ABRE_PARENTESES", "CONDICAO", "FECHA_PARENTESES", "ABRE_CHAVE", "FECHA_CHAVE"]),
            36: ("CONDICAO", ["VALOR", "OPERADOR_LOGICO", "VALOR"]),
            37: ("OPERADOR_LOGICO", ["IGUAL_IGUAL"]),
            38: ("OPERADOR_LOGICO", ["DIFERENTE"]),
            39: ("OPERADOR_LOGICO", ["MAIOR"]),
            40: ("OPERADOR_LOGICO", ["MENOR"]),
            41: ("OPERADOR_LOGICO", ["MAIOR_IGUAL"]),
            42: ("OPERADOR_LOGICO", ["MENOR_IGUAL"]),
            
            # Novas produções - FUNÇÃO
            49: ("FUNCAO", ["FUN", "ABRE_PARENTESES", "PARAMETROS", "FECHA_PARENTESES", "ABRE_CHAVE", "COMANDO", "FECHA_CHAVE"]),
            50: ("PARAMETROS", ["TIPO", "ID", "VIRGULA", "PARAMETROS"]),
            51: ("PARAMETROS", ["TIPO", "ID"]),
            52: ("PARAMETROS", []),  # VAZIO
            
            # Novas produções - CHAMADA DE FUNÇÃO
            53: ("CHAMADA_FUNCAO", ["PONTO_ACESSO", "ID", "ABRE_PARENTESES", "ARGUMENTOS", "FECHA_PARENTESES", "PONTO_VIRGULA"]),
            54: ("ARGUMENTOS", ["VALOR", "VIRGULA", "ARGUMENTOS"]),
            55: ("ARGUMENTOS", ["VALOR"]),
            56: ("ARGUMENTOS", []),  # VAZIO
            
            # Novas produções - FOR
            57: ("FOR", ["FOR", "ABRE_PARENTESES", "ATRIBUICAO_FOR", "PONTO_VIRGULA", "CONDICAO_FOR", "PONTO_VIRGULA", "PASSO", "FECHA_PARENTESES", "ABRE_CHAVE", "BLOCO", "FECHA_CHAVE"]),
            58: ("ATRIBUICAO_FOR", ["ID", "IGUAL", "VALOR"]),
            59: ("ATRIBUICAO_FOR", []),  # VAZIO
            60: ("CONDICAO_FOR", ["ID", "OPERADOR_LOGICO", "VALOR"]),
            61: ("CONDICAO_FOR", []),  # VAZIO
            62: ("PASSO", ["ID", "INCREMENTO"]),
            63: ("PASSO", ["ID", "DECREMENTO"]),
            64: ("PASSO", ["ID", "IGUAL", "EXPRESSAO"]),
            65: ("PASSO", []),  # VAZIO
            
            # Novas produções - WHILE
            66: ("WHILE", ["WHILE", "ABRE_PARENTESES", "CONDICAO", "FECHA_PARENTESES", "ABRE_CHAVE", "BLOCO", "FECHA_CHAVE"]),
        }
        
        # Tabela ACTION otimizada
        self.action = {
            # Estado inicial - Entrada do programa
            0: {
                "INT": "s1", "FLOAT": "s1", "STRING": "s1", "BOOLEAN": "s1", "CHAR": "s1",  # Tipos de dados
                "ID": "s17",          # Identificador
                "OUT": "s3",         # Comando de saída
                "IN": "s4",          # Comando de entrada
                "IF": "s50",         # Comando condicional
                "FUN": "s60",        # Declaração de função
                "PONTO_ACESSO": "s70", # Chamada de função
                "FOR": "s80",        # Loop for
                "WHILE": "s90"       # Loop while
            },
            
            # DECLARAÇÃO E ATRIBUIÇÃO NA DECLARAÇÃO
            1: {"ID": "s5"},         # Tipo seguido de ID
            5: {"PONTO_VIRGULA": "s9", "IGUAL": "s10"},  # ID; ou ID =
            # declaração 
            9: {"$": "r11"},         # Reduz DECLARAR -> TIPO ID ;
            # atribuição
            10: {"ID": "s2", "CONSTANTE": "s2", "ASPAS": "s2"},  # Valores após =
            2: {"PONTO_VIRGULA": "s16", "SOMA": "s20", "SUBTRACAO": "s20", "MULTIPLICACAO": "s20", "DIVISAO": "s20"}, # Reduz ATRIBUIR -> TIPO ID = EXPRESSAO ;
            16: {"$": "r12"},         # Reduz ATRIBUIR -> TIPO ID = EXPRESSAO ;


            # ATRIBUIÇÃO SIMPLES
            20: {"ID": "s18", "CONSTANTE": "s18", "ASPAS": "s18"},  # Valores após =
            18: {"PONTO_VIRGULA": "s19", "SOMA": "s20", "SUBTRACAO": "s20", "MULTIPLICACAO": "s20", "DIVISAO": "s20"},      # Reduz ATRIBUICAO -> ID = EXPRESSAO ;
            19: {"$": "r13"},         # Reduz ATRIBUICAO -> ID = EXPRESSAO ;


            #-------------------------------------------------------

            # Estados para declaração e atribuição (1-10)
            3: {"ABRE_PARENTESES": "s7"},  # OUT(
            4: {"ABRE_PARENTESES": "s8"},  # IN(
            
            # Estados para expressões (6-20)
            6: {"ID": "s11", "CONSTANTE": "s12", "ASPAS": "s13"},  # Valores após =
            7: {"ID": "s14", "ASPAS": "s13"},  # Parâmetros OUT
            8: {"ID": "s15"},        # Parâmetros IN
            
            # Reduções de produções básicas
            
            
            
            
            # Estados para operações (11-17)
            11: {
                "SOMA": "s18", "SUBTRACAO": "s19",     # Operadores aritméticos
                "MULTIPLICACAO": "s20", "DIVISAO": "s21",
                "PONTO_VIRGULA": "s22"                 # Fim de expressão
            },

            # OPERAÇÃO LÓGICA
            12: {"ID": "s13", "CONSTANTE": "s13"},
            13: {
                "IGUAL_IGUAL": "s14", "DIFERENTE": "s14", 
                "MAIOR": "s14", "MENOR": "s14", 
                "MAIOR_IGUAL": "s14", "MENOR_IGUAL": "s14"
            },
            14: {"ID": "s15", "CONSTANTE": "s15"},
            15: {"FECHA_PARENTESES": "r36"},

            # IF (OPERADORES LÓGICA) { }
            # WHILE (OPERADORES LÓGICA) { }
            # OPERAÇÃO LÓGICA -> ID OPERADOR_LOGICO ID

            # Estados para IF (50-59)
            50: {"ABRE_PARENTESES": "s12"},  # if(
            51: {"FECHA_PARENTESES": "s55"},  # if(condição)
            55: {"ABRE_CHAVE": "s56"},  # {
            56: {"FECHA_CHAVE": "s57"},  # }
            57: {"$": "r35"},  # Reduz COMANDO_IF

            # Estados para FUNÇÃO (60-69)
            60: {"ABRE_PARENTESES": "s61"},  # fun(
            61: {  # Parâmetros da função
                "INT": "s62", "FLOAT": "s62", "STRING": "s62", 
                "BOOLEAN": "s62", "CHAR": "s62",
                "FECHA_PARENTESES": "s67"  # Função sem parâmetros
            },
            
            # Estados para CHAMADA DE FUNÇÃO (70-79)
            70: {"ID": "s71"},  # .identificador
            71: {"ABRE_PARENTESES": "s72"},  # .identificador(
            
            # Estados para FOR (80-89)
            80: {"ABRE_PARENTESES": "s81"},  # for(
            81: {"ID": "s82", "PONTO_VIRGULA": "s85"},  # Inicialização for
            
            # Estados para WHILE (90-99)
            90: {"ABRE_PARENTESES": "s91"},  # while(
            91: {"ID": "s92", "CONSTANTE": "s93", "ASPAS": "s94"},  # Condição while
            
            # Estados finais - Reduções para PROGRAMA
            110: {"$": "r1"},   # PROGRAMA -> DECLARAR
            111: {"$": "r2"},   # PROGRAMA -> ATRIBUIR
            112: {"$": "r3"},   # PROGRAMA -> ATRIBUICAO
            113: {"$": "r4"},   # PROGRAMA -> IMPRIMIR
            114: {"$": "r5"},   # PROGRAMA -> LEITURA
            115: {"$": "r6"},   # PROGRAMA -> COMANDO_IF
            116: {"$": "r7"},   # PROGRAMA -> FUNCAO
            117: {"$": "r8"},   # PROGRAMA -> CHAMADA_FUNCAO
            118: {"$": "r9"},   # PROGRAMA -> FOR
            119: {"$": "r10"},  # PROGRAMA -> WHILE
            200: {"$": "acc"}   # Aceita o programa
        }
        
        # Tabela GOTO estendida
        self.goto = {
            0: {
                "PROGRAMA": 200, "DECLARAR": 110, "ATRIBUIR": 111, "ATRIBUICAO": 112, 
                "IMPRIMIR": 113, "LEITURA": 114, "COMANDO_IF": 115, "FUNCAO": 116,
                "CHAMADA_FUNCAO": 117, "FOR": 118, "WHILE": 119, "TIPO": 1
            },
            
            # GOTOs para expressões e valores
            6: {"EXPRESSAO": 40, "VALOR": 11},
            7: {"SAIDA": 41},
            8: {"ENTRADA": 42},
            10: {"EXPRESSAO": 43, "VALOR": 16},
            11: {"OPERACAO": 44},
            16: {"OPERACAO": 44},
            18: {"EXPRESSAO": 45, "VALOR": 27},
            19: {"EXPRESSAO": 45, "VALOR": 27},
            20: {"EXPRESSAO": 45, "VALOR": 27},
            21: {"EXPRESSAO": 45, "VALOR": 27},
            
            # GOTOs para IF
            12: {"CONDICAO": 51},
            50: {"CONDICAO": 51},
            51: {"VALOR": 52, "ESCRITA": 120},
            52: {"OPERADOR_LOGICO": 121},
            55: {"VALOR": 122, "ESCRITA": 123},
            56: {"CONDICAO": 124},
            60: {"ABRE_CHAVE": 125},
            125: {"BLOCO": 126},
            126: {"COMANDO": 127},
            
            # GOTOs para FUNÇÃO
            61: {"PARAMETROS": 128, "TIPO": 62},
            64: {"PARAMETROS": 129, "TIPO": 62},
            66: {"BLOCO": 130},
            
            # GOTOs para CHAMADA DE FUNÇÃO
            72: {"ARGUMENTOS": 131, "VALOR": 73, "ESCRITA": 132},
            76: {"ARGUMENTOS": 133, "VALOR": 73, "ESCRITA": 132},
            
            # GOTOs para FOR
            81: {"ATRIBUICAO_FOR": 134},
            83: {"VALOR": 135, "ESCRITA": 136},
            85: {"CONDICAO_FOR": 137},
            86: {"OPERADOR_LOGICO": 138},
            90: {"PASSO": 139},
            95: {"EXPRESSAO": 140, "VALOR": 97},
            96: {"BLOCO": 141},
            
            # GOTOs para WHILE
            91: {"VALOR": 142, "ESCRITA": 143},
            92: {"OPERADOR_LOGICO": 144},
            95: {"VALOR": 145, "ESCRITA": 143},
            100: {"CONDICAO": 146},
            101: {"BLOCO": 147},
            
            # Estados intermediários
            40: {"PONTO_VIRGULA": "s22"},
            41: {"FECHA_PARENTESES": "s24"},
            42: {"FECHA_PARENTESES": "s25"},
            43: {"PONTO_VIRGULA": "s26"},
            44: {"EXPRESSAO": 46, "VALOR": 27},
            45: {"PONTO_VIRGULA": "s32"},
            46: {"PONTO_VIRGULA": "s47"},
            47: {"$": "r13"}
        }
        
    def analisar(self, entrada):
        """
        Analisa uma entrada usando o algoritmo SLR
        """
        lexico = Lexico()
        lexico.analisar(entrada)
        
        if lexico.erros:
            print("Erros léxicos encontrados:")
            for erro in lexico.erros:
                print(f"  {erro}")
            return False
            
        tokens = lexico.lista_tokens + [Token("$", "$", len(entrada))]
        
        pilha = [0]
        indice = 0
        
        print(f"Analisando: {entrada}")
        print("=" * 80)
        print(f"{'Passo':<5} {'Pilha':<20} {'Entrada':<30} {'Ação':<25}")
        print("=" * 80)
        
        passo = 1
        
        while indice < len(tokens):
            estado_atual = pilha[-1]
            token_atual = tokens[indice].token
            entrada_restante = " ".join([t.token for t in tokens[indice:min(indice+4, len(tokens))]])
            if len(tokens[indice:]) > 4:
                entrada_restante += " ..."
            
            print(f"{passo:<5} {str(pilha):<20} {entrada_restante:<30}", end=" ")
            
            # Verifica se há ação definida
            if estado_atual not in self.action:
                print(f"ERRO - Estado {estado_atual} não existe na ACTION")
                return False
                
            if token_atual not in self.action[estado_atual]:
                print(f"ERRO - Token '{token_atual}' não definido no estado {estado_atual}")
                return False
            
            acao = self.action[estado_atual][token_atual]
            print(f"{acao:<25}")
            
            if acao.startswith('s'):  # Shift
                novo_estado = int(acao[1:])
                pilha.append(novo_estado)
                indice += 1
                
            elif acao.startswith('r'):  # Reduce
                num_reducao = int(acao[1:])
                
                # Busca a produção correspondente
                if num_reducao in self.gramatica:
                    lado_esquerdo, lado_direito = self.gramatica[num_reducao]
                    num_estados = len(lado_direito)
                    
                    # Remove estados da pilha
                    for _ in range(num_estados):
                        if len(pilha) > 1:
                            pilha.pop()
                    
                    # Consulta GOTO
                    estado_topo = pilha[-1]
                    if estado_topo not in self.goto:
                        print(f"ERRO - Estado {estado_topo} não tem GOTO")
                        return False
                        
                    if lado_esquerdo not in self.goto[estado_topo]:
                        print(f"ERRO - GOTO[{estado_topo}][{lado_esquerdo}] não definido")
                        return False
                        
                    novo_estado = self.goto[estado_topo][lado_esquerdo]
                    pilha.append(novo_estado)
                    
                    passo += 1
                    direito_str = ' '.join(lado_direito) if lado_direito else 'ε'
                    print(f"{passo:<5} {str(pilha):<20} {'':30} Reduz: {lado_esquerdo} -> {direito_str}")
                else:
                    print(f"ERRO - Redução r{num_reducao} não encontrada na gramática")
                    return False
                    
            elif acao == 'acc':  # Accept
                print("\nPROGRAMA ACEITO!")
                return True
            else:
                print(f"ERRO - Ação inválida: {acao}")
                return False
            
            passo += 1
            
            if passo > 50:
                print("ERRO - Muitos passos, possível loop")
                return False
        
        return False

def main():
    parser = AnalisadorSLR()
    
    print("=== ANALISADOR SINTÁTICO SLR ESTENDIDO ===")
    print("Com suporte para IF, FUNÇÃO, CHAMADA DE FUNÇÃO, FOR e WHILE\n")
    
    testes = [
        "int x;",
        "int x = 10;", 
        "x = 5;",
        "int result = a + b;",
        "out(variavel);",
        "in(x);",
        "if(x == 10) { }",
        "fun(int x, float y) { z = x + y; }",
        ".calcular(10, 20.5);",
        "for(i = 0; i < 10; i++) { sum = sum + i; }",
        "while(x > 0) { x = x - 1; }"
    ]
    
    for i, teste in enumerate(testes, 1):
        print(f"\n{'='*60}")
        print(f"TESTE {i}: {teste}")
        print('='*60)
        resultado = parser.analisar(teste)
        status = "VÁLIDO" if resultado else "INVÁLIDO"
        print(f"\nResultado: {status}")

if __name__ == "__main__":
    main()