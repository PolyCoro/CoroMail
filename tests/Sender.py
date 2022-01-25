import socket
from src.coder import Coder
from src.config import Config
from base64 import b64decode,b64encode
from Crypto.PublicKey import RSA
from src.app_user import AppUser

if __name__ == "__main__":
    
    IP = "127.0.1.1"
    port = 5000
    cod = Coder("RSA")
    conf = Config("Clement2" , ".")
    if not conf.config_found:
        conf.create_config("www.pornhub.com")
    key = RSA.importKey(b64decode(conf.public_key))
    s = AppUser( IP , port , cod , key )
    
    message = "Coucou" 
    s.send_message( message )
    s.send_message( 'q' ) #close connection