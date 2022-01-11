#!/usr/bin/python3
"""Test cli

Test cases for the CLI of the polycoro project

Todo:
    * Finish the tests

"""

import pytest
import os
import filecmp
from src import cli
from os import remove
from contextlib import redirect_stdout
from docopt import DocoptExit
# Where to put the tests files
TEST_DIRECTORY="tests/"

def test_empty_option():
    """Test the CLI default behavior 

    """
    ret = cli.main()

    for key in ret:
        if ret[key] == True:
            assert False

    assert True

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

    ret = cli.main("--port=123")
    # Doc opt always return a string
    assert  int(ret["--port"])== 123
    ret = cli.main()
    ret["--port"] == 0
    #Test if required arguments are checked for
    with pytest.raises(ValueError):
        ret = cli.main("--port=ghi")

    with pytest.raises(ValueError):
        ret = cli.main("--port=@!")

    with pytest.raises(ValueError):
        ret = cli.main("--port=")
    
    with pytest.raises(ValueError):
        ret = cli.main("--port=-1")


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
    
    #os.remove(TEST_DIRECTORY+'dbg.txt')

def test_send_command():
    """Check that the debug option echoes the app info 

    Must be updated every time there's a new attribute in the CLI

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


    ret = cli.main("send 1ser2 --file testtext.txt")
    assert ret["NAME"] == "1ser2"
    assert ret["--file"] == "testtext.txt"

    # Unexpected behavior but it's a feature
    ret = cli.main("send user1 --f testtext.txt")
    assert ret["NAME"] == "user1"
    assert ret["--file"] == "testtext.txt"
        # Doc opt always return a string
  
