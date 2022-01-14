

# TODO : Remove this once a proper app user class has been developped
class app_user :
    def __init__(self,name,password,pubkey,ip):
        self.name = name 
        self.password = password 
        self.pubkey = pubkey
        self.ip = ip