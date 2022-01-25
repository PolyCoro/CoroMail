import appUser
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA512, SHA384, SHA256, SHA, MD5
from Crypto import Random

class Message :
    """
    This class is used to define a message.

    Attributes:
        sender (appUser): 
        receiver (appUser): 
        signature (bytes): Signature corresponding to the text variable 

    """ 

    def __init__(self, sender, receiver, text, signature):
        """ Fill the class attributes

        Args:
            sender (appUser): 
            receiver (appUser): 
            signature (bytes): Signature corresponding to the text variable 
        """
        self.sender = sender
        self.receiver = receiver
        if isinstance(text, str) == False :
            raise TypeError("Message has to be a string")
        else :
            self._text = text
        self.signature = signature
 
    def set_sender(self,sender):
        if isinstance(sender, appUser.appUser) == False:
            raise TypeError("Sender has to be a appUser")
        else :
            self.sender = sender 

    def set_receiver(self,receiver):
        if isinstance(receiver, appUser.appUser) == False:
            raise TypeError("Sender has to be a appUser")
        else :
            self.receiver = receiver 

    """
    #Se trouve ici pour l'instant mais va etre deplacé dans Session
    def sign(message, priv_key, hashAlg="SHA-256"):
        
        signer = PKCS1_v1_5.new(priv_key)
        if (hashAlg == "SHA-512"):
            digest = SHA512.new()
        elif (hashAlg == "SHA-384"):
            digest = SHA384.new()
        elif (hashAlg == "SHA-256"):
            digest = SHA256.new()
        elif (hashAlg == "SHA-1"):
            digest = SHA.new()
        else:
            digest = MD5.new()
        digest.update(message)
        return signer.sign(digest)
    """

    def checkSignature(self, hashAlg):
        signer = PKCS1_v1_5.new(self.sender.get_publickey())

        if (hashAlg == "SHA-512"):
            digest = SHA512.new()
        elif (hashAlg == "SHA-384"):
            digest = SHA384.new()
        elif (hashAlg == "SHA-256"):
            digest = SHA256.new()
        elif (hashAlg == "SHA-1"):
            digest = SHA.new()
        else:
            digest = MD5.new()
        tmp = bytes(self._text, 'utf-8')
        digest.update(tmp)
        return signer.verify(digest, self.signature)


if __name__ == '__main__':

    hashAlg = "SHA-256"

    msg = "Hello Tony, I am Jarvis!"
    msg = bytes(msg, 'utf-8') #Conversion message en bytes

    #Génération des clées
    key = RSA.generate(2048) #private key
    public_key = key.publickey() #public key

    #Signature
    signer = PKCS1_v1_5.new(key)
    if (hashAlg == "SHA-512"):
        digest = SHA512.new()
    elif (hashAlg == "SHA-384"):
        digest = SHA384.new()
    elif (hashAlg == "SHA-256"):
        digest = SHA256.new()
    elif (hashAlg == "SHA-1"):
        digest = SHA.new()
    else:
        digest = MD5.new()
    digest.update(msg)
    signature = signer.sign(digest)

    """signature = Message.sign(msg, key, hashAlg)
    print(type(signature))"""
    msg = "Hello Tony, I am Jarvis!"
    #Creation du message
    msg1 = Message(0,0,msg,signature)

    #Creation de l'utilisateur
    usr = appUser.appUser("Alexandra",msg1,"127.0.0.1",public_key)
    msg1.set_sender(usr)
    
    #Verify
    verify = msg1.checkSignature(hashAlg)
    print(verify)

    #Ajout d'un caractère dans la signature - Doit FAIL
    msg1.signature = msg1.signature + b'a'
    verify = msg1.checkSignature(hashAlg)
    print(verify)