#!/usr/bin/python3
"""Test cli

Test cases for the CLI of the polycoro project

Todo:
    * Finish the tests

"""

import pytest
import os
import filecmp
from src.app_user import *
from src.contacts import contacts

from os import remove
from contextlib import redirect_stdout
from docopt import DocoptExit
import sqlite3
# Where to put the tests files
TEST_DIRECTORY="tests/"
DB_NAME = "contacts.db"


tst_name = "someone"
tst_pwd = "password"
tst_pkey = "pkey"
tst_ip = "127.0.0.0"
tst_usr = app_user(tst_name,tst_pwd,tst_pkey,tst_ip)
add_tst_name = "added"
add_tst_pwd = "pwd"
add_tst_pkey = "pkey"
add_tst_ip = "127.0.0.0"
add_usr = app_user(add_tst_name,add_tst_pwd,add_tst_pkey,add_tst_ip)
tst_users = [tst_usr,add_usr]
need_db = 0

def test_empty_db_name():
    """
Check that empty or wrong names for the database raise an error
"""
    with pytest.raises(ValueError):
        contacts("",None)

def test_db_creation():
    """
Check that empty or wrong names for the database raise an error
"""
    ct = contacts(DB_NAME,tst_usr)
    
    ret = ct.cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='"+tst_usr.name+"'")
    # Verify that a table is created
    assert ct.cur.fetchall()[0][0] == tst_usr.name
    
    #Verify if the fields are createds
    fields = ct.cur.execute("SELECT name FROM PRAGMA_TABLE_INFO('"+tst_usr.name+"')" ).fetchall()
    i = 0
    for colname in COLUMN_NAMES :
        assert fields[i][0] == colname 
        i += 1
        
def test_add_user():
    """
Check that empty or wrong names for the database raise an error
"""
    need_db = 1
    ct = contacts(DB_NAME,tst_usr)
    ct.add_user(add_usr)
    query =  "SELECT * FROM "+tst_usr.name+" WHERE "+USERNAME_COL_NAME + " = '" +add_usr.name +"'"
    
    data = ct.cur.execute(query).fetchall()
    usr = app_user(data[0][0],data[0][1],data[0][2],data[0][3])
    assert usr.name == add_tst_name
    assert usr.password == add_tst_pwd
    assert usr.ip == add_tst_ip
    assert usr.pubkey == add_tst_pkey

def test_add_user_unique():
    """
Check that each user has a different name
"""
    need_db = 1
    ct = contacts(DB_NAME,tst_usr)
    ct.add_user(add_usr)
    with pytest.raises(sqlite3.IntegrityError):
          ct.add_user(add_usr)


def test_get_user():
    """
Check that empty or wrong names for the database raise an error
"""
    need_db = 1
    ct = contacts(DB_NAME, tst_usr)
    ct.add_user(add_usr)
    query =  "SELECT * FROM "+tst_usr.name+" WHERE "+USERNAME_COL_NAME + " = '" +add_usr.name +"'"

    data = ct.cur.execute( query).fetchall()
    usr = app_user(data[0][0],data[0][1],data[0][2],data[0][3])
    assert usr.name == add_tst_name
    assert usr.password == add_tst_pwd
    assert usr.ip == add_tst_ip
    assert usr.pubkey == add_tst_pkey
    
def test_get_users():
    """
Check that every user in a database are retrieved
"""
    need_db = 1
    ct = contacts(DB_NAME, tst_usr)
    ct.add_user(tst_usr)
    ct.add_user(add_usr)
    users = ct.get_users()
    i = 0
    for usr in tst_users:
        assert usr.name  == users[i].name 
        assert usr.password  ==users[i].password 
        assert usr.ip  == users[i].ip 
        assert usr.pubkey  ==users[i].pubkey 
        i += 1

@pytest.fixture(autouse=True)
def teardown():

    if need_db:
        ct = contacts(DB_NAME,tst_usr)
    yield

    if(os.path.exists(DB_NAME)):
        print("I was here")
        os.remove(DB_NAME)

if __name__ == '__main__':

    main() == None
