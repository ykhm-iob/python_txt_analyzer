import unittest # type: ignore
from sizeconverter import File_Size_Converter # type: ignore

class Test_Conversions(unittest.TestCase):
    '''
    Test class that checks if kb and mb conversion
    are happening properly and rounding to the 2ths place.
    '''
    def test_check_kb(self):
        '''
        Tests for convert_to_kb().
        '''
        checker = File_Size_Converter()
        checked = checker.convert_to_kb(1024)
        kb_test = 1024
        kb_test_result = kb_test / 1024
        kb_test_result_rounded = round(kb_test_result, 2)
        self.assertEquals(checked, kb_test_result_rounded)

    def test_check_mb(self):
        '''
        Tests for convert_to_mb().
        '''
        checker = File_Size_Converter()
        checked = checker.convert_to_mb(2097152)
        mb_test = 2097152
        mb_test_result = mb_test / 1048576
        mb_test_result_rounded = round(mb_test_result, 2)
        self.assertEquals(checked, mb_test_result_rounded)

if __name__ == '__main__':
    unittest.main()
    input("Press ENTER to continue...")
