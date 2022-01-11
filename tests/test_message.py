import unittest
import pytest

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA512, SHA384, SHA256, SHA, MD5
from Crypto import Random

import sys
#import src
#from src.coder import Coder

import sys
sys.path.append("/home/deac/workworkwork/CoroMail/src")
from appUser import appUser
from message import Message

class TestFuncs(unittest.TestCase):


	def test_good_verify(self):
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
		msg = "Hello Tony, I am Jarvis!"
		#Creation du message
		msg1 = Message(0,0,msg,signature)

		#Creation de l'utilisateur
		usr = appUser("Alexandra",msg1,"127.0.0.1",public_key)
		msg1.set_sender(usr)

		#Verify
		verify = msg1.checkSignature(hashAlg)
		self.assertEqual( True , verify )
	    

	def test_wrong_verify(self):
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
		msg = "Hello Tony, I am Jarvis!"
		#Creation du message
		msg1 = Message(0,0,msg,signature)

		#Creation de l'utilisateur
		usr = appUser("Alexandra",msg1,"127.0.0.1",public_key)
		msg1.set_sender(usr)

		#Verify
		#Ajout d'un caractère dans la signature - Doit FAIL
		msg1.signature = msg1.signature + b'a'
		verify = msg1.checkSignature(hashAlg)
		self.assertEqual( False , verify )

	def test_verify_different_algo(self):
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
		msg = "Hello Tony, I am Jarvis!"
		#Creation du message
		msg1 = Message(0,0,msg,signature)

		#Creation de l'utilisateur
		usr = appUser("Alexandra",msg1,"127.0.0.1",public_key)
		msg1.set_sender(usr)

		#Verify
		#different hash algo
		hashAlg = "SHA-1"
		verify = msg1.checkSignature(hashAlg)
		self.assertEqual( False , verify )

	def test_set_sender(self):
		hashAlg = "SHA-256"
		msg = "Hello Tony, I am Jarvis!"

		#Creation du message
		msg1 = Message(0,0,msg,"")

		with pytest.raises(TypeError):
			msg1.set_sender("usr")
	    


if __name__ == '__main__':
	unittest.main()