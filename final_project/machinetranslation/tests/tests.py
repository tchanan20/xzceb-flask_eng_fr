import unittest

from translator import frenchToEnglish, englishToFrench

class TestEnglishToFrench(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(englishToFrench(""), "") # test when no input is given the output is null.
        self.assertEqual(englishToFrench("Hello"), "Bonjour")  # test when "Hello" is given as input the output is "Bonjour".

class TestFrenchToEnglish(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(frenchToEnglish(""), "") # test when no input is given the output is null.
        self.assertEqual(frenchToEnglish("Bonjour"), "Hello")  # test when "Bonjour" is given as input the output is "Hello".

unittest.main()