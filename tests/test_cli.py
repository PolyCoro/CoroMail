#!/usr/bin/python3
"""Test cli

Test cases for the CLI of the polycoro project

Todo:
    * Finish the tests

"""

import pytest
import os
import filecmp
from src import cli, contacts
from os import remove
from contextlib import redirect_stdout
from docopt import DocoptExit

# Where to put the tests files
TEST_DIRECTORY="tests/"

def test_empty_option():
    """Test the CLI default behavior 

    """
    with pytest.raises(DocoptExit):
        ret = cli.main("")


def test_s_option():
    """Test the s option in the CLI.

    """
    ret = cli.main("-s")
    assert ret["-s"]== True

def test_server_option():
    """Check that the two option ored give the same results.

    """
    ret = cli.main("--server")
    assert ret["--server"]== True


def test_server_equivalency_to_s():
    """Check that the two option ored give the same results.

    """
    ret = cli.main("--server")
    assert ret["-s"]== True
    ret = cli.main("-s")
    assert ret["--server"]== True

def test_port_option():
    """Check that the port option is taken into account if provided

    """
    with pytest.raises(DocoptExit):
        ret = cli.main("--port=123")

    with pytest.raises(DocoptExit):
        ret = cli.main("--port")
        
    
    #Test if required arguments are checked for
    with pytest.raises(ValueError):
        ret = cli.main("-s --port=ghi")

    with pytest.raises(ValueError):
        ret = cli.main("-s --port=@!")

    with pytest.raises(ValueError):
        ret = cli.main("-s --port=")
    
    with pytest.raises(ValueError):
        ret = cli.main("-s --port=-1")


def test_debug_option():
    """Check that the debug option echoes the app info 

    Must be updated every time there's a new attribute in the CLI

    """

    with open(TEST_DIRECTORY+'dbg.txt', 'w') as f:
        with redirect_stdout(f):
            ret = cli.main("-d")
            
    #Cant read from write opened file
    with open(TEST_DIRECTORY+'dbg.txt', 'r') as f:
        with open(TEST_DIRECTORY+'expected_dbg.txt', 'r') as fe:
            assert(filecmp.cmp(f.name,fe.name))
    
    os.remove(TEST_DIRECTORY+'dbg.txt')

def test_send_command():
    """Check that the send command get the right parameters when launched or otherwhile fails 

    """
    with pytest.raises(DocoptExit):
        ret = cli.main("send")

    with pytest.raises(DocoptExit):
        ret = cli.main("send user1")

    with pytest.raises(DocoptExit):
        ret = cli.main("send user1 -f")

    with pytest.raises(DocoptExit):
        ret = cli.main("send -f")

    with pytest.raises(DocoptExit):
        ret = cli.main("send --file afile.txt")

    ret = cli.main("send user1 testtext")
    assert ret["NAME"] == "user1"
    assert ret["TEXT"] == "testtext"

    ret = cli.main("send 1ser2 --file " + TEST_DIRECTORY+ "testtext.txt")
    assert ret["NAME"] == "1ser2"
    assert ret["--file"] == TEST_DIRECTORY+"testtext.txt"

    # Unexpected behavior but it's a feature
    ret = cli.main("send user1 --f "+TEST_DIRECTORY+"testtext.txt")
    assert ret["NAME"] == "user1"
    assert ret["--file"] == TEST_DIRECTORY+"testtext.txt"
        # Doc opt always return a string
  
def test_check():
    """Check that the check command is rightly understood
    """
    with pytest.raises(DocoptExit):
        ret = cli.main("check")


    ret = cli.main("check user1")
    assert ret["NAME"] == "user1"
    assert ret["check"] == True

    ret = cli.main("check 1ser1 --port=3")
    assert ret["NAME"] == "1ser1"
    assert ret["check"] == True
    assert int(ret["--port"]) == 3

def test_getpub():
    """Check that the get public key command has the same behavior as expected 
    """

    with pytest.raises(DocoptExit):
        ret = cli.main("getpub")

    ret = cli.main("getpub user1")
    print(ret)
    assert ret["NAME"] == "user1"
    assert ret["getpub"] == True

    ret = cli.main("getpub user1 --port=01")
    print(ret)
    assert ret["NAME"] == "user1"
    assert ret["getpub"] == True
    assert int(ret["--port"]) == 1


def test_show_user():
    """
Check that empty or wrong names for the database raise an error
"""
    # ct = contacts(DB_NAME,tst_usr)
    
    # with open(TEST_DIRECTORY+'show_test.txt', 'w') as f:
    #     with redirect_stdout(f):
    #         ret = cli.main("show "+ tst_usr.name)

    # with open(TEST_DIRECTORY+'expected_show_test.txt', 'r') as fe:
    #         assert(filecmp.cmp(f.name,fe.name))

    # ret = cli.main("show user1")