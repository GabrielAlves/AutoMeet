# AutoMeet

Um programa que realiza automaticamente o processo de entrada em reuniões do meet. 

## Motivo

Eu queria facilitar a minha entrada nas aulas da universidade que são realizadas através do meet.

## Pré-requisitos

* Python 3.*

## Instalação

* Clone o repositório: `git clone https://github.com/GabrielAlves/AutoMeet.git`
* Entre no repositório clonado : `cd AutoMeet`
* Instale as dependências : `pip install -r requirements.txt`

## Restrições

Infelizmente, o programa é bastante instável, apresentando diversas restrições. Algumas das restrições identificadas foram:

* O programa procura exatamente as imagens que foram recortadas, então quaisquer ações que mudem a maneira que as imagens aparecem na tela, tais como zoom do navegador, idioma do navegador, ou até mesmo a cor dos botões, podem fazer com que elas não sejam encontradas. Como exemplificação, as imagens que eu coloquei na pasta img foram extraídas do navegador firefox, versão desktop, em português, sob zoom 100%, por volta do mês de junho; 
* Os links sempre são abertos através do navegador definido como padrão, então as imagens a serem buscadas devem ser extraídas desse navegador;
* Se o próprio meet alterar alguma imagem, o programa não será mais capaz de encontra-la, e a única solução é recortar uma nova;

## Como usar

* Insira os links das reuniões na lista `self.links_do_meet` presente no arquivo `link.py`. Por padrão, o índice 0 da lista contém os links da segunda-feira, o indíce 1, da terça-feira, e assim por diante. Em cada índice, há um dicionário que faz o mapeamento entre horários e links;
    * Defina o horário do link nas tuplas. Uma reunião que começa às 7 e encerra às 12, por exemplo, deve ter a tupla definida como (7, 12);
    * Defina o link dentro das aspas;
* Se for necessário mudar as imagens recortadas, adicione elas em alguma pasta, e atualize o caminho delas nas listas presentes no arquivo `auto_meet.py`;
* Se todos os passos anteriores já tiverem sido feitos, basta executar o arquivo `auto_meet.py` nos horários das reuniões;