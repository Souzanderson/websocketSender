import json
from websocket import create_connection
import json

class WebSocketConfig:
    def __init__(self, location_config_file = "config.websocket.json"):
        self.__conf__ = json.load(open(location_config_file, 'r')) or {}
    
    @property
    def URL(self):
        return self.__conf__.get("url")

class WebsocketMessage:
    def __init__(self):
        self.subject = None
        self.sender = None
        self.topics = []
        self.payload = None
    
    @staticmethod
    def fromRecv(message_text):
        try:
            data = json.loads(message_text) 
            obj = WebsocketMessage()
            obj.subject = data.get('subject')
            obj.sender = data.get('sender')
            obj.topics = data.get('topics')
            obj.payload = data.get('payload')
            return obj
        except Exception as e:
            print(f'[ERROR] Error in WebsocketMessage =>  {e}')
            return WebsocketMessage()
    
    def toDict(self):
        return {
            "subject" : self.subject,
            "sender" : self.sender,
            "topics" : self.topics,
            "payload" : self.payload,
        }

class SendMessageWS():
    def __init__(self, message:WebsocketMessage, config: WebSocketConfig):
        self.__message__ = message
        self.__config__ = config
    
    def send(self):
        try:
            print(f"{self.__config__.URL}?hashcode={self.__message__.sender}&topics=system")
            ws = create_connection(f"{self.__config__.URL}?hashcode={self.__message__.sender}&topics=system")
            ws.send(json.dumps(self.__message__.toDict(), indent=4))
        except Exception as e:
            print("[ERROR] Erro ao enviar notificação => %s" %str(e))

    
    