from datetime import datetime, timedelta

class DatasBr:
    def __init__(self):
        self.momento_cadastro = datetime.today()
    def __str__(self):
        return self.momento_cadastro.strftime("%d/%m/%Y %H:%M")
    def mes_cadastro(self):
        meses_do_ano = ["Janeiro", "Fevereiro","Março", "Abril",
                        "Maio", "Junho", "Julho", "Agosto",
                        "Setembro", "Outubro", "Novembro", "Dezembro"]
        mes_cadastro = self.momento_cadastro.month
        return meses_do_ano[mes_cadastro-1]
    def dia_semana(self):
        dias_semana = ["Segunda-feira", "Terça-feira", "Quarta-feira",
                       "Quinta-feira", "Sabado", "Domingo"]
        dia_semana = self.momento_cadastro.weekday()
        return dias_semana[dia_semana]
    def tempo_cadastro(self): #Essa classe não tem função prática, contudo, foi aplicada a título de aprendizagem
        tempo_cadastro = (datetime.today() + timedelta(days = 30)) - self.momento_cadastro
        return tempo_cadastro

