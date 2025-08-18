class Token:
    def __init__(self, token, lexema, pos):
        self.token = token
        self.lexema = lexema
        self.pos = pos

    def __str__(self):
        return f"Token: {self.token}, Lexema: {self.lexema}, Posição: {self.pos}"
