from src.contacts import *
from src.app_user import *
from src.config import *

class Session :
    def __init__(self,db_path=DEFAULT_DB_NAME,username="",password="",conf_path=default_config_directory):
        """ Create a session object. Requires a config and a database   
        
        Args :
            db_path(str) : Path to the database file
            username(str) : Session owner name
            password(str) : Password. Irrelevant for now
        """
        if username == None or username == "":
            raise ValueError
        if db_path == None or db_path == "":
            raise ValueError

        self.config = Config(username)
        if not self.config :
            # check the config is set up
            pass
        #TODO : Check that password is needed here
        #TODO : How is the IP retrieved ?
        self.current_user = app_user(self.Config.username,"",self.Config.public_key,"127.0.0.1")
        self.contacts = contacts(db_path,self.current_user) 

    def generate_signature(self):
        pass
    def get_contacts(self):
        return self.contacts
        pass
        
    def add_myself_to_server(self):
        pass