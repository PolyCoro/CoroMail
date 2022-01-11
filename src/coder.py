import sys
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

class Coder :
    """
    This class is used to encrypt a message.

    Attributes:
        algo (str): encryption algorithm chosen.

    """ 

    def __init__(self, algo):
        """ Fill the class attributes

        Args:
            algo (str): encryption algorithm choose."""

        self.algo = algo
 
    def code(self, text, publickey) :
        """ Encrypt a message.

        Args:
            text (str): text to encrypt.
            publickey (RsaKey): public key
        
        Returns:
            The encypted message
        """
        if isinstance(text,str) == False:
        	raise TypeError("message has to be a string not a %s "(type(text)))

        if len(text) <= 0 :
            raise ValueError("message is empty")

        if isinstance(publickey,RSA._RSAobj) == False:
        	raise TypeError("publickey has to be a Crypto.PublicKey.RSA._RSAobj not a %s "(type(publickey)))

        if (self.algo == "RSA"):
            tmp = bytes(text, 'utf-8')
            encryptor = PKCS1_OAEP.new(publickey)
            encrypted_msg = encryptor.encrypt(tmp)
        return encrypted_msg