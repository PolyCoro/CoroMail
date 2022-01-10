import src
from src.config import Config
import unittest
import os.path
from os import path

class TestFuncs(unittest.TestCase):

	def test_creation_file(self):
		c1 = Config( os.getcwd() , "http://url_du_server.com" , "Clement" )
		self.assertEqual( path.exists( os.getcwd() + "Clement.conf" ) , True )
		self.assertEqual( c1.get_conf_path() , os.getcwd() + "/Clement.conf" )
		self.assertEqual( c1.get_username() , "Clement" )
		self.assertEqual( len( c1.get_private_key() ) , 1024  )
		self.assertEqual( len( c1.get_public_key() ) , 1024  )
		self.assertEqual( c1.get_CAS_url() , "http://url_du_server.com" )

	def test_load_file(self):
		c1 = Config( os.getcwd() , "http://url_du_server.com" , "Clement" )
		c2 = Config( os.getcwd() , "http://url_du_server.com" , "Clement" )
		self.assertEqual( path.exists( os.getcwd() + "Clement.conf" ) , True )
		self.assertEqual( c2.get_conf_path() , os.getcwd() + "/Clement.conf" )
		self.assertEqual( c2.get_username() , "Clement" )
		self.assertEqual( len( c2.get_private_key() ) , 1024  )
		self.assertEqual( len( c2.get_public_key() ) , 1024  )
		self.assertEqual( c2.get_private_key() , c1.get_private_key()  )
		self.assertEqual( c2.get_public_key() , c1.get_public_key()  )
		self.assertEqual( c2.get_CAS_url() , "http://url_du_server.com" )

if __name__ == '__main__':
	unittest.main()
	