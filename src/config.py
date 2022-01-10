import os.path
from os import path
from Crypto.PublicKey import RSA

#Config constructor
#Inputs : path to conf file , URL of the CAS , username of the user
class Config():

    def __init__(self , conf_path , CAS_url , username ):

        #if conf file, load infos from it
        if path.exists( conf_path + "/" + username + ".conf" ):
            self.conf_path = conf_path + "/" + username + ".conf"
            file = open(self.conf_path , "r")
            text = file.readlines()
            
            j = 0
            s = ""
            for l in (text):
                if( l == '\n' ):
                    if( j == 0 ):
                        self.username = s
                    elif( j == 1 ):
                        self.public_key = s
                    elif( j == 2 ):
                        self.private_key = s
                    else:
                        self.CAS_url = s
                    j += 1
                    s = ""
                else:
                    s += l            
                            
            file.close()

        #else, generate keys and create conf file   
        else:    
            self.conf_path = conf_path + "/" + username + ".conf" 
            self.CAS_url = CAS_url
            self.private_key = self.generate_keys()[0]
            self.public_key = self.generate_keys()[1]
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
        file = open(self.conf_path , "w")
        file.write( self.username + '\n')
        file.write( self.public_key + '\n')
        file.write( self.private_key + '\n')
        file.write( self.CAS_url + '\n')
        file.close()

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
