
import sys
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP


class Coder :
	"""
	This class is used to encrypt a message.
    Attributes:
        algo (str): encryption algorithm choose.

    """ 

	def __init__(self, algo):
		""" Fill the class attributes
		Args:
			algo (str): encryption algorithm choose."""
		self.algo = algo
 
	def code(self,text,publickey) :
		if len(text) == 0 :
			return "FAIL"
		if (self.algo == "RSA"):
			tmp = bytes(text, 'utf-8')
			encryptor = PKCS1_OAEP.new(publickey)
			encrypted_msg = encryptor.encrypt(tmp)
		return encrypted_msg


if __name__ == '__main__':
	
	message = "test"
	key = RSA.generate(1024)
	public_key = key.publickey()
	encrypt = Coder("RSA")
	encrypted_msg = encrypt.code(message,public_key)
	print(encrypted_msg)
	decryptor = PKCS1_OAEP.new(key)
	decoded_msg = decryptor.decrypt(encrypted_msg)
	decoded_msg = decoded_msg.decode('utf-8')
	print(decoded_msg)


