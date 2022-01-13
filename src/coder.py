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
        if isinstance(text, str) == False:
            raise TypeError("Message has to be a string")

        if len(text) <= 0 :
            raise ValueError("message is empty")

        if (self.algo == "RSA"):
            tmp = bytes(text, 'utf-8')
            encryptor = PKCS1_OAEP.new(publickey)
            try:
                encrypted_msg = encryptor.encrypt(tmp)
            except AttributeError:
                raise TypeError("Invalid key format")
        return encrypted_msg