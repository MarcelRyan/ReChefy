import sys
sys.path.insert(1, r'./src/database')
from unittest.mock import Mock
import databaseFunc

def test_initializeTable():
    db_connector = Mock()
    databaseFunc.initializeTable(db_connector)

def test_connectToDatabase():
    assert databaseFunc.connectToDatabase("test.db") == None

def test_addAlat():
    db_connector = Mock()
    databaseFunc.initializeTable(db_connector)
    databaseFunc.addAlat(db_connector, "tes")

def test_addBahan():
    db_connector = Mock()
    databaseFunc.initializeTable(db_connector)
    databaseFunc.addBahan(db_connector, "tes")