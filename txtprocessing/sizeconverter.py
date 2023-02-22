class File_Size_Converter():
    '''
    Class that converts an int (bytes) into
    KB/MBs, rounded to the 2nd decimal place.
    '''
    def __init__(self) -> None:
        pass

    def check_size(self, file_size: int) -> float:
        '''
        Function which checks the file size being passed
        to send it to the "correct" conversion function.

        Arguments:
          int file_size -- an int meant to represent a
          file's bytesize.

        Variables:
          int converted_size -- file_size after converting
          via func calls.

        Return:
          int converted_size -- formatted file size
        '''
        try:
            if file_size >= 1024 and file_size < 1048576:
                converted_size = self.convert_to_kb(file_size)
            else:
                converted_size = self.convert_to_mb(file_size)
        except TypeError:
            print("You must pass an int/float file size.")
        return converted_size

    def convert_to_kb(self, file_size: int) -> float:
        '''
        Function that divides an int by 1024 and rounds it
        to get a byte size formatted via kilobytes.

        Arguments:
          int file_size -- an int meant to represent
         a file's bytesize.

        Variables:
          int file_size_kb -- file_size divided by 1024
          int round_file_size_kb -- file_size_kb rounded
          to the 2 place.

        Return:
          int round_file_size_kb -- file_size_kb rounded
          to the 2 place.
        '''
        try:
            file_size_kb = file_size / 1024
            rounded_file_size_kb = round(file_size_kb, 2)
        except ZeroDivisionError:
            print("Zero is an invalid file size!")
        except TypeError:
            print("You must pass an int/float file size.")
        return rounded_file_size_kb

    def convert_to_mb(self, file_size: int) -> float:
        '''
        Function that divides an int by 1024 and rounds it
        to get a byte size formatted via kilobytes.

        Arguments:
          int file_size -- an int meant to represent
          a file's bytesize.

        Variables:
          int file_size_mb -- file_size divided by 1024*1024
          int round_file_size_mb -- file_size_mb rounded
          to the 2 place.

        Return:
          int round_file_size_mb -- file_size_mb rounded
          to the 2 place.
        '''
        try:
            file_size_mb = file_size / 1048576
            rounded_file_size_mb = round(file_size_mb, 2)
        except ZeroDivisionError:
            print("Zero is an invalid file size!")
        except TypeError:
            print("You must pass an int/float file size.")
        return rounded_file_size_mb

if __name__ == '__main__':
    sample_size = 1024
    big_sample_size = 6000000
    sample_object = File_Size_Converter()
    print("Sample Size 1:", sample_size, "Bytes")
    print("sample Size 2:", big_sample_size, "Bytes")
    new_sample_size = sample_object.check_size(sample_size)
    new_big_sample_size = sample_object.check_size(big_sample_size)
    print("Sample Size 1, Converted:", new_sample_size, "KB")
    print("sample Size 2, Converted:", new_big_sample_size, "MB")
    input("Press ENTER to continue...")
