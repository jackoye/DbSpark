# test_dbspark.py
"""
Tests for DbSpark module.
"""

import unittest
from dbspark import DbSpark

class TestDbSpark(unittest.TestCase):
    """Test cases for DbSpark class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = DbSpark()
        self.assertIsInstance(instance, DbSpark)
        
    def test_run_method(self):
        """Test the run method."""
        instance = DbSpark()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
