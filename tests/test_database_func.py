import sys
from unittest.mock import Mock
from src.database.databaseFunc import *

def test_initializeTable():
    db_connector = Mock()
    initializeTable(db_connector)

def test_connectToDatabase():
    assert connectToDatabase("test.db") == None

def test_addAlat():
    db_connector = Mock()
    initializeTable(db_connector)
    addAlat(db_connector, "tes")

def test_addBahan():
    db_connector = Mock()
    initializeTable(db_connector)
    addBahan(db_connector, "tes")