import unittest

import sys
sys.path.append('../..')

from machinetranslation import translator

class TestTranslator(unittest.TestCase): 
    def test_french_to_english(self): 
        self.assertEqual(translator.french_to_english('Bonjour'), 'Hello') 

    def test_french_to_english_empty(self): 
        self.assertIsNone(translator.french_to_english('')) 

    def test_french_to_english_null(self): 
        self.assertIsNone(translator.french_to_english('')) 

    def test_english_to_french(self): 
        self.assertEqual(translator.english_to_french('Hello'), 'Bonjour') 

    def test_english_to_french_empty(self): 
        self.assertIsNone(translator.english_to_french('')) 

    def test_english_to_french_null(self): 
        self.assertIsNone(translator.english_to_french(None)) 

unittest.main()