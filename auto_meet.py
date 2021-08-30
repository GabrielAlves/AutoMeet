import webbrowser
import time
from mensagem import Mensagem
from link import Link
import pyautogui

class AutoMeet:
    def entrar_no_meet(self):
        imagens = ["img/botao-alternar-conta.png", "img/botao-email-dominio-ufpi.png", "img/botao-permitir-camera.png", "img/botao-ativar-camera.png", "img/botao-ativar-microfone.png", ["img/botao-participar-sala.png", "img/botao-participar-sala2.png", "img/botao-participar-sala3.png"]]
        self.acessar_imagens(imagens)

    def acessar_imagens(self, imagens):
        for imagem in imagens:
            resultado_da_busca = self.procurar_imagem_continuamente(imagem)

            # TODO: Mostrar mensagem de erro, caso a imagem não seja encontrada
            if resultado_da_busca is None:
                # Mensagem("Error", "Imagem não encontrada", f"A imagem \"{imagem}\" não foi encontrada dentro do tempo limite")
                return None

            AutoMeet.clicar_na_tela(resultado_da_busca)

    # Obs: As "imagens" que são listas buscam resolver um caso específico em que há mais de uma possibilidade de imagem para a mesma busca.
    def procurar_imagem_continuamente(self, imagem):
        timer_de_busca = 30
        delay_entre_buscas = 0.1

        if type(imagem) is list:
            i = 0

        while timer_de_busca >= 0:
            if type(imagem) is list:
                resultado_da_busca = self.buscar_imagem_na_tela(imagem[i])

            else:
                resultado_da_busca = self.buscar_imagem_na_tela(imagem)

            if resultado_da_busca is not None:
                return resultado_da_busca

            # Alterna a imagem da lista para que seja procurada na próxima iteração.
            if type(imagem) is list:
                i += 1

                if i == len(imagem):
                    i = 0

            time.sleep(delay_entre_buscas)
            timer_de_busca -= delay_entre_buscas
        
        return None

    def buscar_imagem_na_tela(self, imagem):
        try:
            local = pyautogui.locateOnScreen(imagem, confidence = 0.9)
            posicao = pyautogui.center(local)
            return posicao
        
        except Exception as e:
            # print(e)
            return None

    @staticmethod
    def clicar_na_tela(posicao):
        pyautogui.click(posicao)

    def entrar_no_chat(self):
        imagens = [["img/botao-chat-sem-mensagem.png", "img/botao-chat-com-mensagem.png"], "img/caixa-de-texto-do-chat.png"]
        self.acessar_imagens(imagens)

    def escrever_mensagem_no_chat(self, mensagem = Link.retornar_cumprimento_da_hora_atual()):
        self.entrar_no_chat()
        pyautogui.write(mensagem, interval = 0.25)
        pyautogui.press("enter")
    
if __name__ == "__main__":
    link_atual = Link().selecionar_link_atual() 
    auto_meet = AutoMeet()

    if link_atual:  
        webbrowser.open(link_atual) 
        auto_meet.entrar_no_meet()
        auto_meet.escrever_mensagem_no_chat()

    else:
        Mensagem("error", "Sem registros", "Não há links cadastrados para esse horário")