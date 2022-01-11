import os.path
from os import path
from Crypto.PublicKey import RSA
import json

#Config constructor
#Inputs : path to conf file , URL of the CAS , username of the user
class Config():

    def __init__(self , conf_path , CAS_url , username ):

        self.username = ""
        self.public_key = ""
        self.private_key = ""
        self.CAS_url = ""

        #if conf file, load infos from it
        if path.exists( conf_path + "/" + username + ".json" ):
            self.conf_path = conf_path + "/" + username + ".json"
            data = {}
            data['infos'] = []
            with open(self.conf_path) as json_file:
                data = json.load(json_file)
                for p in data['infos']:
                    self.username = p['username']
                    self.public_key = p['public_key']
                    self.private_key = p['private_key']
                    self.CAS_url = p['CAS_url']            

        #else, generate keys and create conf file   
        else:
            self.conf_path = conf_path + "/" + username + ".json" 
            self.CAS_url = CAS_url
            self.private_key = self.generate_keys()[0][29:-26] #delete headers
            self.public_key = self.generate_keys()[1][32:-30] #delete headers
            self.username = username
            self.create_conf_file()
        
    #generate private and public keys of the user with RSA algorithm        
    def generate_keys(self):
        key = RSA.generate(1024)
        public_key = key.publickey().exportKey("PEM").decode()
        private_key = key.exportKey("PEM").decode()
        return (public_key , private_key)

    #create conf file and fill it with infos generated before
    def create_conf_file(self):
        data = {}
        data['infos'] = []
        data['infos'].append({
            'username': self.username,
            'public_key': self.public_key,
            'private_key': self.private_key,
            'CAS_url': self.CAS_url
        })

        with open(self.conf_path , 'w') as file:
            json.dump(data, file , indent = 4)

    #return public key of the user
    def get_public_key(self):
        return self.public_key

    #return private key of the user
    def get_private_key(self):
        return self.private_key

    #return username of the user
    def get_username(self):
        return self.username

    #return url of the cas
    def get_CAS_url(self):
        return self.CAS_url

    #return configuration file path
    def get_conf_path(self):
        return self.conf_path
