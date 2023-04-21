from validate_docbr import CPF
from validate_docbr import CNPJ

class Documento:
    @staticmethod
    def cria_documento(documento):
        if len(documento) == 11:
            return Doc_CPF(documento)
        elif len(documento) == 14:
            return Doc_CNPJ(documento)
        else:
            raise ValueError("Quantidade de dígitos do documento está incorreta!")

class Doc_CPF:
    def __init__(self, documento):
        if self.valida(documento):
            self.cpf = documento
        else:
            raise ValueError("CPF é inválido!")
    def __str__(self):
        return self.formata()
    def valida(self, documento):
        validador = CPF()
        return validador.validate(documento)
    def formata(self):
        mascara = CPF()
        return mascara.mask(self.cpf)

class Doc_CNPJ:
    def __init__(self, documento):
        if self.valida(documento):
            self.cnpj = documento
        else:
            raise ValueError("CNPJ é inválido!")
    def __str__(self):
        return self.formata()
    def valida(self, documento):
        validador = CNPJ()
        return validador.validate(documento)
    def formata(self):
        mascara = CNPJ()
        return mascara.mask(self.cnpj)


