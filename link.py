from datetime import datetime
import calendar

class Link:
    def __init__(self):
        calendar.setfirstweekday(0) # Garante que o primeiro indice corresponde aos links da segunda-feira. Pode ser modificado, desde que você altera a ordem dos links adequadamente.
        self.links_do_meet = [
                            {(8, 12) : "Insira o link aqui", (14, 18) : "Insira o link aqui"},
                            {(8, 12) : "Insira o link aqui", (14, 18) : "Insira o link aqui"},
                            {(8, 12) : "Insira o link aqui", (14, 18) : "Insira o link aqui"},
                            {(8, 12) : "Insira o link aqui", (14, 18) : "Insira o link aqui"},
                            {(8, 12) : "Insira o link aqui", (14, 18) : "Insira o link aqui"},
                            {(8, 12) : "Insira o link aqui"},
                            {}
                            ]

    @staticmethod
    def receber_data_atual():
        data_atual = datetime.now()
        ano_atual = data_atual.year
        mes_atual = data_atual.month
        dia_atual = data_atual.day

        return {"ano" : ano_atual, "mes" : mes_atual, "dia" : dia_atual}

    @staticmethod
    def receber_hora_atual():
        return datetime.now().hour

    @staticmethod
    def retornar_cumprimento_da_hora_atual():
        hora_atual = Link.receber_hora_atual()

        if hora_atual < 12:
            return "Bom dia!"

        elif hora_atual < 18:
            return "Boa tarde!"

        else:
            return "Boa noite!"


    def selecionar_links_de_hoje(self):
        data_atual = Link.receber_data_atual()
        dia_da_semana_atual = calendar.weekday(data_atual["ano"], data_atual["mes"], data_atual["dia"])
        links_de_hoje = self.links_do_meet[dia_da_semana_atual]

        return links_de_hoje

    def selecionar_link_atual(self):
        links_de_hoje = self.selecionar_links_de_hoje()
        hora_atual = Link.receber_hora_atual()

        link_atual = None
        for horario in links_de_hoje:
            hora_de_inicio = horario[0]
            hora_de_termino = horario[1]

            if hora_de_inicio <= hora_atual < hora_de_termino:
                link_atual = links_de_hoje[(horario)]
                break

        return link_atual