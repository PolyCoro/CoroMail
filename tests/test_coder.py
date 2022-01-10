import unittest
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

import sys
import src
from src.coder import Coder


class TestFuncs(unittest.TestCase):


	def test_code(self):
		message = "coucou les amis"
		key = RSA.generate(1024)
		public_key = key.publickey()
		encrypt = Coder("RSA")
		encrypted_msg = encrypt.code(message,public_key)
		decryptor = PKCS1_OAEP.new(key)
		decoded_msg = decryptor.decrypt(encrypted_msg)
		decoded_msg = decoded_msg.decode('utf-8')
		self.assertEqual( message , decoded_msg )

		message = ""
		key = RSA.generate(1024)
		public_key = key.publickey()
		encrypt = Coder("RSA")
		encrypted_msg = encrypt.code(message,public_key)
		self.assertEqual( encrypted_msg , "FAIL" )

		message = "Té~st @V#èc Kàr@c&Reœ $péçùiaux1µ*5"
		key = RSA.generate(1024)
		public_key = key.publickey()
		encrypt = Coder("RSA")
		encrypted_msg = encrypt.code(message,public_key)
		decryptor = PKCS1_OAEP.new(key)
		decoded_msg = decryptor.decrypt(encrypted_msg)
		decoded_msg = decoded_msg.decode('utf-8')
		self.assertEqual( message , decoded_msg )


if __name__ == '__main__':
	unittest.main()