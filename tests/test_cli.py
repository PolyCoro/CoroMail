#!/usr/bin/python3
"""Test cli

Test cases for the CLI of the polycoro project

Todo:
    * Finish the tests

"""

import pytest
from src import cli

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
