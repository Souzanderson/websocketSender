
'''
####################################################################################
################## INSTRUÇÕES PARA UTILIZAÇÃO DO SENDER WEBSOCKET ################## 
####################################################################################
#                                                                                  #
#   - Coloque o arquivo ./library/senderws.py em uma pasta em seu projeto;         #
#   - Crie um arquivo config.websocket.json na raíz do seu projeto;                #
#   - Dentro dele, crie uma chave "url" contendo o endereço do websocket;          #
#   - importe sendersws.py no seu projeto, como feito abaixo;                      #
#   - Siga o exemplo de utilização abaixo;                                         #
#                                                                                  #
####################################################################################
####################################################################################

'''

import json
from library.senderws import SendMessageWS, WebSocketConfig, WebsocketMessage


if __name__ == '__main__':
    #Instanciar o objeto de mensagem que será enviado
    message = WebsocketMessage()
    #Adicionar o dicionário contendo os valores que deseja enviar (no exemplo peguei os valores de um arquivo .json pra mock test)
    message.payload=json.load(open("test.json",'r'))
    #Propriedade que indica quem enviou, deve ser a hash do emissário, id, identificação usada qualquer
    message.sender = "backend"
    #Propriedade que indica o assunto do envio (pode ficar em branco se não for utilizar)
    message.subject = "reload maquinas"
    #topicos aos quais a mensagem será entregue
    message.topics = ["maquinas"]
    
    ''' Instanciar a classe de envio e passar por injeção de dependências as instâncias:
    
            - Da mensagem;
            - Da classe de configuração 
            (indica onde seu arquivo de configuração está, passada sem argumentos se
            o arquivo for config.websocket.json e estiver na raíz do projeto);
            
        Por fim chamar o método send() pra enviar os dados pro servidor de websocket configurado no arquivo de configuração;
    '''
    SendMessageWS(message,WebSocketConfig()).send()
    