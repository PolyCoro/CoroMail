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
from src.session import *
# Where to put the tests files



def test_empty_db_name():
    """
Check that empty or wrong names for the database raise an error
"""
    with pytest.raises(ValueError):
        Session()
