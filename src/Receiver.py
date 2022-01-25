import socket
from src.decoder import Decoder
from src.config import Config
from Crypto.PublicKey import RSA
from base64 import b64decode,b64encode

class AppUser:
    def __init__(self, IP , port, crypt, key):
        self.IP = IP
        self.port = port
        self.crypt = crypt
        self.key = key    

    def send_message(self , message):
        csocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        csocket.connect( (self.IP, self.port) )
        message = self.crypt.code( message , self.key );
        csocket.send( bytes(message , "utf-8") )

    def receive_message(self):
        serverSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        serverSock.bind((self.IP, self.port))
        serverSock.listen(2)
        data = ""

        while data != 'q':
            conn, addr = serverSock.accept()
            data = conn.recv(4096)
            if data != "":
                data = self.crypt.decode( data , self.key )
            if data == 'q':
                print( "Fermeture de la connexion ..." )
            else:    
                print("Un message a été reçu : ", data)
        serverSock.close()

if __name__ == "__main__":
    
    IP = "127.0.1.1"
    port = 5000
    decod = Decoder("RSA")
    conf = Config("Clement2" , ".")
    if not conf.config_found:
        conf.create_config("www.pornhub.com") 
    key = RSA.importKey(b64decode(conf.private_key))
    s = AppUser( IP , port , decod , key )
    
    s.receive_message()