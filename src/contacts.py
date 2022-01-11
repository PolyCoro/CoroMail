#!/usr/bin/python3
"""Contacts

Manage contacts from the database
"""
import logging
from docopt import docopt
import sqlite3
TABLE_NAME = "Polycoro"
COLUMN_NAMES = ('name','public_key','ip')
# Not necessarily useful
USER_NAME= "me"
# TODO : Remove this once a proper app user class has been developped
class app_user :
    def __init__(self,name,password,ip):
        self.name = name 
        self.password = password 
        self.ip = ip

class contacts:
    def __init__(self,db_name):
        if db_name == "":
            raise ValueError
        try :
            conn = sqlite3.connect(db_name)
        except ConnectionError:
            self.cur = conn.cursor()
            raise 

    def add_user(usr) :
        query = "INSERT INTO "+TABLE_NAME+":"+ USER_NAME + "(" +COLUMN_NAMES[0]
        var_field = "(?"
        for col in COLUMN_NAMES[1:] :
            query +=   " , " + col 
            var_field += ",?"

        query += ") values " + var_field+")"
        cur.execute(query,(usr.name,usr.password,usr.public_key))

if __name__ == "__main__" :
    Contacts =contacts("")