from txtprocessing.txtreader import Text_File #type: ignore
from txtprocessing.txtconverter import Text_Conversion #type: ignore
from txtprocessing.sizeconverter import File_Size_Converter #type: ignore
from txtprocessing.txtletterhistogram import Text_To_LetterHistogram #type: ignore

class Main_Class():
    '''
    Class which is designed around making use of the txtprocessing
    library folder. It is entirely dependent on txtprocessing.
    '''
    def __init__(self) -> None:
        pass

    def text_analysis(self) -> None:
        '''
        Function that makes use of txtreader.py to scan and
        analyze a sample.txt file.

        Variables:
          obj test -- Dependent on the Text_File class, runs its methods
          obj file_size_convert -- Dependent on the File_Sizer_Converter
          class, and uses its methods to convert file_size to kb/mb
          instead of raw bytes.
          int file_size -- contains the total bytes of sample.txt
          int characters -- contains the total character count of sample.txt
          list lines -- a list with two ints, [0] is total lines with
          linebreaks and [1] is without linebreaks
          str file_extension -- contains sample.txt's file extension
          str file_path -- contains the directory for sample.txt
        '''
        test = Text_File()
        test.set_filepath("sample.txt")
        file_size = test.total_file_size()
        file_size_convert = File_Size_Converter()
        converted_size = file_size_convert.check_size(file_size)
        lines = test.total_lines()
        characters = test.total_characters()
        file_extension = test.get_file_extension()
        file_path = test.get_filepath()
        print("Total lines with line-breaks:", lines[0])
        print("Total lines without line-breaks:", lines[1])
        print("Total file-size:", converted_size, "KBs")
        print("Current file path:", file_path)
        print("Current file extension type:", file_extension)
        print("Total characters:", characters)
        print("")

    def text_converting(self, data_set) -> None:
        '''
        Function that makes use of txtconverter.py to take a pandas df
        and convert it to both csv and json files.

        Arguments:
          obj data_set -- a pandas dataframe/series to be converted
          into both csv and json files.

        Variables:
          obj conversions -- Dependent on the Text_Conversion class,
          runs its methods.
          obj data_set -- obj that gives "obj conversions" a df/series
          to convert.
        '''
        conversions = Text_Conversion()
        conversions.convert_to_csv(data_set)
        print("sample.txt's letter histogram has been converted to a csv!")
        conversions.convert_to_json(data_set)
        print("sample.txt's letter histogram has been converted to a json!")
        print("Check out the root folder to see converted_data_set.")

    def text_letter_histogram(self) -> object:
        '''
        Function that makes use of txtletterhistogram.py to take a
        .txt and convert it to a letter histogram.

        Variables:
          obj sample -- Dependent on the Text_To_LetterHistogram class,
          runs its methods.
        '''
        sample = Text_To_LetterHistogram()
        letter_histogram = sample.create_letter_histogram("sample.txt")
        print("The following is sample.txt's letter histogram. \n")
        sample.print_letter_histogram(letter_histogram)
        return letter_histogram

    def execute(self) -> None:
        '''
        Function that calls text_analysis() and text_converting().
        Exists to make the non-OOP monolith easier on the
        eyes to understand.
        '''
        self.text_analysis()
        letter_hist = self.text_letter_histogram()
        letter_hist
        self.text_converting(letter_hist)


if __name__ == '__main__':
    main = Main_Class()
    print("The following is an analysis of sample.txt. \n")
    main.execute()
    input("Press ENTER to continue...")
