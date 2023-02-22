import string #type: ignore
import collections #type: ignore
import pandas as pd #type: ignore

class Text_To_LetterHistogram():
    '''
    Class which is designed around processing a .txt file into
    a letter histogram using pandas series (1 dimension array).
    It will return the letter histogram and you can use that
    returned letter histogram to be printed in a nice formatting
    if desired via print_letter_histogram() method.
    '''
    def create_letter_histogram(self, file_path) -> object:
        '''
        Function that creates a letter histogram via .txt file.

        Arguments:
          str file_path -- The desired filepath to convert into
          a letter histogram.

        Variables:
          obj txt_collection -- the file_path's character count
          via collections.
          obj converted_pd_series -- the file_path's letter histogram.

        Return:
          obj converted_pd_series -- the file_path's letter histogram.
        '''
        try:
            with open (file_path, 'r') as txt_file:
                txt_collection = collections.Counter(txt_file.read().lower())
                converted_pd_series = pd.Series(txt_collection, index=sorted(string.ascii_lowercase))
                converted_pd_series.fillna(value="0", inplace=True)
                converted_pd_series = converted_pd_series.astype(int)
                return converted_pd_series
        except FileNotFoundError:
            print("The current file could not be found or isn't readable!")
        

    def print_letter_histogram(self, series) -> None:
        '''
        Function that prints a letter histogram. Makes use
        of string formatting to be visually presentable in cmd.
        '''
        for letter in string.ascii_letters:
            if letter in series:
                print('{}: {}'.format(letter, series[letter]))

if __name__ == '__main__':
    print("The following is a letter histogram from sample.txt.\n")
    main_sample = Text_To_LetterHistogram()
    letter_histogram = main_sample.create_letter_histogram("sample.txt")
    main_sample.print_letter_histogram(letter_histogram)
    input("Press ENTER to continue...")
