import src
from src.config import *
import unittest
import os.path
from os import path

class TestFuncs(unittest.TestCase):

	def test_creation_file(self):
		c1 = Config("Clement", os.getcwd())
		self.assertEqual(c1.config_found, False)
		c1.create_config("127.0.0.1")
		self.assertEqual( path.exists( os.getcwd() + "/Clement.json" ) , True )
		os.remove(os.getcwd() + "/Clement.json")
		self.assertEqual( c1.filename , os.getcwd() + "/Clement.json" )
		self.assertEqual( c1.username , "Clement" )
		self.assertEqual( c1.CAS_url , "127.0.0.1" )
		self.assertNotEqual(c1.public_key, "")
		self.assertNotEqual(c1.private_key, "")

	def test_load_file(self):
		self.assertEqual( path.exists( os.getcwd() + "/Clem.json" ) , False )
		c1 = Config("Clem", os.getcwd())
		self.assertEqual(c1.config_found, False)
		if c1.config_found == False:
			c1.create_config("localhost")
		self.assertEqual( path.exists( os.getcwd() + "/Clem.json" ) , True )
		c2 = Config( "Clem", os.getcwd())
		os.remove(os.getcwd() + "/Clem.json")
		self.assertEqual(c2.config_found, True)
		self.assertEqual( c2.filename , os.getcwd() + "/Clem.json" )
		self.assertEqual( c2.username , "Clem" )
		self.assertNotEqual(c2.public_key, "")
		self.assertNotEqual(c2.private_key, "")
		self.assertEqual( c2.CAS_url , "localhost" )
	
	def test_no_url(self):
		#c1 = Config("no_url", os.getcwd() + "/tests")
		with self.assertRaises(BadConfigError):
			Config("no_url",os.getcwd() + "/tests")

	def test_no_pk(self):
		#c1 = Config("no_url", os.getcwd() + "/tests")
		with self.assertRaises(BadConfigError):
			Config("no_pk",os.getcwd() + "/tests")

	def test_no_privk(self):
		#c1 = Config("no_url", os.getcwd() + "/tests")
		with self.assertRaises(BadConfigError):
			Config("no_privk",os.getcwd() + "/tests")

	def test_bad_json(self):
		with self.assertRaises(BadConfigError):
			Config("bad_json", os.getcwd() + "/tests")

if __name__ == '__main__':
	unittest.main()
	