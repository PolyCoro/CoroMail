import socket
from src.app_user import AppUser
from src.decoder import Decoder
from src.config import Config
from Crypto.PublicKey import RSA
from base64 import b64decode,b64encode

if __name__ == "__main__":
    
    IP = "192.168.69.106"
    port = 5000
    decod = Decoder("RSA")
    conf = Config("Clement2" , ".")
    if not conf.config_found:
        conf.create_config("localhost") 
    key = RSA.importKey(b64decode(conf.private_key))
    s = AppUser( IP , port , decod , key )
    
    s.receive_message()