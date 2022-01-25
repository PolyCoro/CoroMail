import os.path
from os import path
from pathlib import Path
from Crypto.PublicKey import RSA
import json

default_config_directory = str(Path.home()) + "/.config/coromail"

#Config constructor
#Inputs : path to conf file , URL of the CAS , username of the user
class Config():

    def __init__(self, username, conf_path=default_config_directory):
        """ Create config object. If config file is found, fill the class
            attributes. Otherwise, self.config_found is set to False and you
            should call self.create_config()

        Args:
            username (str): username
            conf_path (str): path to configuration file
        """
        self.username = username
        self.public_key = ""
        self.private_key = ""
        self.CAS_url = ""
        self.config_found = True
        self.filename = conf_path + "/" + username + ".json"
        
        data = {}
        data['infos'] = []

        if path.exists(self.filename):
            with open(self.filename, "r") as file:
                try:
                    data = json.load(file)
                except Exception:
                    raise BadConfigError("Bad JSON format")
            for p in data['infos']:
                try:
                    self.public_key = p['public_key']
                except KeyError:
                    raise BadConfigError("Public key not found in config")
                try:
                    self.private_key = p['private_key']
                except KeyError:
                    raise BadConfigError("Private key not found in config")
                try:
                    self.CAS_url = p['CAS_url']
                except KeyError:
                    raise BadConfigError("CAS url not found in config")
        else:
            self.config_found = False


    def create_config(self, CAS_url):
        """ Create configuration file.

            Args:
                CAS_url(str): url of the CAS server
        """

        self.CAS_url = CAS_url
        keys = self._generate_keys()
        self.private_key = keys[1][32:-29] #delete headers
        self.public_key = keys[0][27:-25] #delete headers
        self._create_conf_file()
        
    def _generate_keys(self):
        """ Generate private and public keys of the user with RSA algorithm
        """
        key = RSA.generate(2048)
        public_key = key.publickey().exportKey("PEM").decode()
        private_key = key.exportKey("PEM").decode()
        return (public_key , private_key)

    def _create_conf_file(self):
        """ Create conf file and fill it with infos generated before
        """
        data = {}
        data['infos'] = []
        data['infos'].append({
            'username': self.username,
            'public_key': self.public_key,
            'private_key': self.private_key,
            'CAS_url': self.CAS_url
        })

        with open(self.filename , 'w') as file:
            json.dump(data, file , indent = 4)

class BadConfigError(Exception):
    """ Error raised if a config file cannot be read"""
    pass