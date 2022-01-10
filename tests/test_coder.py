import unittest
from Crypto.PublicKey import RSA

import sys
sys.path.append("/home/deac/workworkwork/CoroMail/src")
from coder import Coder


class TestFuncs(unittest.TestCase):


	def test_code(self):
		message = "coucou les amis"
		key = RSA.generate(1024)
		public_key = key.publickey()
		encrypt = Coder("RSA")
		encrypted_msg = encrypt.code(message,public_key)
		decoded_msg = key.decrypt(encrypted_msg)
		decoded_msg = decoded_msg.decode('utf-8')
		self.assertEqual( message , decoded_msg )

		message = ""
		key = RSA.generate(1024)
		public_key = key.publickey()
		encrypt = Coder("RSA")
		encrypted_msg = encrypt.code(message,public_key)
		self.assertEqual( encrypted_msg , "FAIL" )

		message = "Tést @Vèc Kàr@c&Re $péçiaux15"
		key = RSA.generate(1024)
		public_key = key.publickey()
		encrypt = Coder("RSA")
		encrypted_msg = encrypt.code(message,public_key)
		decoded_msg = key.decrypt(encrypted_msg)
		decoded_msg = decoded_msg.decode('utf-8')
		self.assertEqual( message , decoded_msg )

		


if __name__ == '__main__':
	unittest.main()