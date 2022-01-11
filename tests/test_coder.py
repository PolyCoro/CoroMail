import unittest
import pytest
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
		with pytest.raises(ValueError): encrypt.code(message, public_key)

		message = "Té~st @V#èc Kàr@c&Reœ $péçùiaux1µ*5"
		key = RSA.generate(1024)
		public_key = key.publickey()
		encrypt = Coder("RSA")
		encrypted_msg = encrypt.code(message,public_key)
		decryptor = PKCS1_OAEP.new(key)
		decoded_msg = decryptor.decrypt(encrypted_msg)
		decoded_msg = decoded_msg.decode('utf-8')
		self.assertEqual( message , decoded_msg )


	def test_non_key(self):
		key = "This is not a key"
		text = "Text to encrypt"
		coder = Coder("RSA")
		with pytest.raises(TypeError):
			coder.code(text, key)

	def test_empty_key(self):
		text = "Text to encrypt"
		coder = Coder("RSA")
		with pytest.raises(TypeError):
			coder.code(text, "")
	
	def test_empty_text(self):
		key = RSA.generate(1024)
		public_key = key.publickey()
		coder = Coder("RSA")
		with pytest.raises(ValueError):
			coder.code("", key)
	
	def test_non_text(self):
		key = RSA.generate(1024)
		public_key = key.publickey()
		coder = Coder("RSA")
		rList = [1, 2, 3, 4, 5]
		arr = bytes(rList)
		with pytest.raises(TypeError):
			coder.code(arr, key)
	
	def test_text_too_long(self):
		key = RSA.generate(1024)
		public_key = key.publickey()
		coder = Coder("RSA")
		text = "a" * 100
		with pytest.raises(ValueError):
			coder.code(text, key)

	def test_text_not_too_long_2048(self):
		key = RSA.generate(2048)
		public_key = key.publickey()
		coder = Coder("RSA")
		text = "a" * 100
		coder.code(text, key)

	def test_text_too_long_2048(self):
		key = RSA.generate(2048)
		public_key = key.publickey()
		coder = Coder("RSA")
		text = "a" * 1000
		with pytest.raises(ValueError):
			coder.code(text, key)



if __name__ == '__main__':
	unittest.main()