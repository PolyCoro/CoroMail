#!/usr/bin/python3
"""Contacts

Manage contacts from the database
"""
import logging
from docopt import docopt
import sqlite3
from src.app_user import *
# Not necessarily useful
DB_NAME = "contacts.db"
USERNAME_COL_NAME = 'name'
COLUMN_NAMES = (USERNAME_COL_NAME,"password","pubkey","ip")

class contacts:
    """ Contacts classes to manage the database from the client
    """
    conn = None
    def __init__(self,db_path,usr):
        if db_path == "" or usr == None:
            raise ValueError
        
        try :
            self.conn = sqlite3.connect(db_path)
        except ConnectionError:
            raise 
        self.cur = self.conn.cursor()
        query = "create table if not exists "+usr.name+" ("+COLUMN_NAMES[0] + " UNIQUE"
        for col in COLUMN_NAMES[1:] :
            query +=   ", " + col 
        query += ');'
        self.cur.execute(query)
        self.owner = usr

    def add_user(self,usr) :
        """Insert an app_user into the database
        Args:
		usr_name (usr) : an app_user 
		
	""" 
        query = "INSERT INTO "+ self.owner.name + "(" +COLUMN_NAMES[0]
        var_field = "(?"
        for col in COLUMN_NAMES[1:] :
            query +=   " , " + col 
            var_field += ",?"

        query += ") values " + var_field +")"
 
        self.cur.execute(query,(usr.name,usr.password,usr.pubkey,usr.ip))
        self.conn.commit()

    def get_user(self,usr_name) :
        """ Return an app_user from the database
		Args:
		usr_name (String) : the name of the user we want to retrieve
		
		Returns:
            appUser: the user retrieved from the database
	""" 
        query = "SELECT * FROM "+self.owner.name+" WHERE "+USERNAME_COL_NAME + " = '" +usr_name +"'"
        fields = self.cur.execute(query).fetchall()
        print(fields[0])
        return app_user(fields[0][0],fields[0][1],fields[0][2],fields[0][3])

    def get_users(self) :
        """ Return all the app users from the database

		Returns:
            appUser[]: the users retrieved from the database
	""" 
        query = "SELECT * FROM "+self.owner.name
        fields = self.cur.execute(query).fetchall()
        users = []
        for usr_info in fields :
            users.append(app_user(usr_info[0],usr_info[1],usr_info[2],usr_info[3]))

        return users


if __name__ == "__main__" :
    Contacts =contacts("")