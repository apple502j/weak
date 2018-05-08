"""Test WEAK."""
import unittest
from string import ascii_lowercase as lowers
from weak import crypto

class CryptoKeyTest(unittest.TestCase):
    """Tests for CryptoKey"""
    def test_length(self):
        """Test that lengths are equal"""
        self.assertEqual(len(crypto.generateKeys()[0]), 4 * (26 ** 2))
        self.assertEqual(len(crypto.generateKeys()[1]), 4 * (26 ** 2))
        self.assertEqual(len(crypto.generateKeys()), 2)

    def test_chars_count(self):
        """Test that the number of chars is correct"""
        key = crypto.generateKeys()
        for i in key:
            for char in lowers:
                self.assertEqual(i.count(char), 104)

if __name__ == '__main__':
    unittest.main()
