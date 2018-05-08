from weak import crypto
import unittest
from string import ascii_lowercase as lowers
import site

class CryptoKeyTest(unittest.TestCase):
    def test_length(self):
        self.assertEqual(len(crypto.generateKeys()[0]),4*(26**2))
        self.assertEqual(len(crypto.generateKeys()[1]),4*(26**2))
        self.assertEqual(len(crypto.generateKeys()),2)

    def test_chars_count(self):
        key=crypto.generateKeys()
        for n in range(2):
            for char in lowers:
                self.assertEqual(key[n].count(char),104)

if __name__ == '__main__':
    unittest.main()
