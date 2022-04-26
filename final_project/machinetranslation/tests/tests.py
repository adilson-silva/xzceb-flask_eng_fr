import unittest

import sys
sys.path.append('../..')

from machinetranslation import translator

class TestTranslator(unittest.TestCase): 
    def test_french_to_english_assert_equal(self): 
        self.assertEqual(translator.french_to_english('Bonjour'), 'Hello', "frenchToEnglish - assertEqual") 

    def test_french_to_english_assert_not_equal(self): 
        self.assertNotEqual(translator.french_to_english('Bonjour'), 'Hi', "frenchToEnglish - assertNotEqual") 

    def test_french_to_english_empty(self): 
        self.assertIsNone(translator.french_to_english(''), "frenchToEnglish - Empty") 

    def test_french_to_english_null(self): 
        self.assertIsNone(translator.french_to_english(None), "frenchToEnglish - Null") 

    def test_english_to_french_assert_equal(self): 
        self.assertEqual(translator.english_to_french('Hello'), 'Bonjour', "englishToFrench - assertEqual") 

    def test_english_to_french_assert_not_equal(self): 
        self.assertNotEqual(translator.english_to_french('Hello'), 'Hallo', "englishToFrench - assertNotEqual") 

    def test_english_to_french_empty(self): 
        self.assertIsNone(translator.english_to_french(''), "englishToFrench - Empty") 

    def test_english_to_french_null(self): 
        self.assertIsNone(translator.english_to_french(None), "englishToFrench - assertNull") 

unittest.main()