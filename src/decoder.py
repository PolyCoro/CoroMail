from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP


class Decoder : 

	def __init__(self, algo):
	    self.algo = algo


	def decode(self,message,privatekey):

		if (self.algo == "RSA"):
			decryptor = PKCS1_OAEP.new(privatekey)
			decrypted_msg = decryptor.decrypt(message)
		return str(decrypted_msg, "utf-8")