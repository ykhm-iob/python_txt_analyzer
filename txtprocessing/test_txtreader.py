import unittest # type: ignore
from txtreader import Text_File # type: ignore

class Test_TextReader(unittest.TestCase):
    '''
    Test class that checks if txtreader.py
    returns correct values.
    '''
    def test_extensions(self):
        '''
        Tests that get_file_extension() returns the correct
        extension type.
        '''
        checker = Text_File()
        checker.set_filepath("test_sample.txt")
        checked = checker.get_file_extension()
        self.assertEquals(checked, ".txt")

    def test_lines(self):
        '''
        Tests that total_lines() returns a list with lines
        with and without breaks.
        '''
        checker = Text_File()
        checker.set_filepath("test_sample.txt")
        checked = checker.total_lines()
        self.assertEquals(checked, [17, 11])

    def test_character_count(self):
        '''
        Tests that total_characters() returns an int that
        is a total character count.
        '''
        checker = Text_File()
        checker.set_filepath("test_sample.txt")
        checked = checker.total_characters()
        self.assertEquals(checked, 1290)


    def test_file_size(self):
        '''
        Tests that total_file_size() returns an int that
        is the total file size in bytes.
        '''
        checker = Text_File()
        checker.set_filepath("test_sample.txt")
        checked = checker.total_file_size()
        self.assertEquals(checked, 1310)

if __name__ == '__main__':
    unittest.main()
