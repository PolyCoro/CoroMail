import src
import sys
from src.main import main
from src.decoder import Decoder
import unittest
import Crypto
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

def code(text,publickey) :
		if len(text) == 0 :
			return "FAIL"
		tmp = bytes(text, 'utf-8')
		encrypted_msg = publickey.encrypt(tmp,sys.getsizeof(tmp))
		return encrypted_msg

class tests_decoder(unittest.TestCase):	

	def test_decode(self):
		key = RSA.generate(1024)
	
		#chiffrage
		public_key = key.publickey()
		encryptor = PKCS1_OAEP.new(public_key)
		decryptor = Decoder("RSA")

		clear_msg1 = bytes("Hello World", 'utf-8')
		encrypted_msg1 = encryptor.encrypt(clear_msg1)
		decrypted_msg1 = decryptor.decode(encrypted_msg1,key)
		self.assertEqual(decrypted_msg1, clear_msg1)
		
		f2 = open('tests/special_caracters.txt', 'r')
		clear_msg2 = bytes(f2.read(), 'utf-8')
		f2.close()
		encrypted_msg2 = encryptor.encrypt(clear_msg2)
		decrypted_msg2 = decryptor.decode(encrypted_msg2, key)
		self.assertEqual(decrypted_msg2, clear_msg2)
		
		f3 = open('tests/lorem_ipsum.txt', 'r')
		clear_msg3 = bytes(f3.read(), 'utf-8')
		f3.close()
		encrypted_msg3 = encryptor.encrypt(clear_msg3)
		decrypted_msg3 = decryptor.decode(encrypted_msg3, key)
		self.assertEqual(decrypted_msg3, clear_msg3)
		

if __name__ == '__main__':
	unittest.main()