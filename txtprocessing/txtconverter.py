import pandas as pd #type: ignore

class Text_Conversion():
    '''
    Class that contains functions to convert a
    pandas df/series to different file types for use.
    '''
    def convert_to_csv(self, data_set: object) -> None:
        '''
        Function that converts a df/series to a .csv file.

        Variables:
          obj file_conversion -- uses pandas to convert to a .csv
        '''
        try:
            file_conversion = data_set
            file_conversion.to_csv('converted_data_set.csv') # type: ignore
        except pd.errors.EmptyDataError:
            print("An exception occured. Please double-check your argument.")
        except pd.errors.ParserError:
            print("An exception occured. Please double-check your argument.")
        except Exception:
            print("An exception occured. Please double-check your argument.")

    def convert_to_json(self, data_set: object) -> None:
        '''
        Function that converts a df/series to a .json file.

        Variables:
          obj file_conversion -- uses pandas to convert to a .json
        '''
        try:
            file_conversion = data_set
            file_conversion.to_json('converted_data_set.json') #type: ignore
        except pd.errors.EmptyDataError:
            print("An exception occured. Please double-check your argument.")
        except pd.errors.ParserError:
            print("An exception occured. Please double-check your argument.")
        except Exception:
            print("An exception occured. Please double-check your argument.")

if __name__ == '__main__':
    main = Text_Conversion()
    sample_series = pd.Series([1, 2, 3, 4, 5])
    main.convert_to_csv(sample_series)
    print("sample_series has been converted to a .csv file!")
    main.convert_to_json(sample_series)
    print("sample_series has been converted to a .json file!")
    input("Press ENTER to continue...")
