import pathlib as pb #type: ignore

class Text_File():
    '''
    Text_File class takes a file_path and reads from it to
    analyze it in multiple ways.
    '''
    def __init__(self) -> None:
        self.file_path = None

    def set_filepath(self, file_path: str) -> None:
        '''
        Function that updates the class' file_path variable.

        Variable:
          str new_file_path -- updated file path from the user
        '''
        new_file_path = file_path
        self.file_path = new_file_path # type: ignore

    def get_filepath(self):
        '''
        Function that returns the full file path.

        Variables:
          Path target_path -- str that contains self.file_path's
          path.

        Return:
          Path target_path -- the file's full file path.
        '''
        target_path = pb.Path.cwd().joinpath(self.file_path)
        return target_path

    def get_file_extension(self) -> str:
        '''
        Function that returns the file extension (.txt etc).

        Variables:
          str file_extension -- str that contains self.file_path's
          extension.

        Return:
          str file_extension -- the file's extension.
        '''
        file_extension = self.get_filepath().suffix
        return file_extension

    def view_file(self) -> None:
        '''
        View file prints out a file to the console. Knows what to
        print by setting the file_path.
        '''
        try:
            with open (self.file_path, 'r') as txt_file: # type: ignore
                for line in txt_file:
                    print(line)
        except FileNotFoundError:
            print("The current file could not be found or isn't readable!")

    def total_lines(self) -> list:
        '''
        Function that goes through a .txt file and returns a list that
        contains the total lines with, and without linebreaks ("\n")

        Variables:
          list count_data -- two item list that holds i++ of lines in
          a .txt file. cd[0] is all lines, cd[1] is lines w.o breaks.

        Returns:
          list count_data -- total lines
        '''
        count_data = [0,0]
        try:
            with open (self.file_path, 'r') as text_file: # type: ignore
                for line in text_file:
                    count_data[0] += 1
                    if line != "\n":
                        count_data[1] += 1
        except FileNotFoundError:
            print("The current file could not be found or isn't readable!")
        return count_data

    def total_characters(self) -> int:
        '''
       Function that uses open (without with) on an obj to get the
        len of a .txt file which will return the total characters including
        spaces within the .txt.

        Variables:
          obj file -- an open command to read the length of
          file_content --
          int file_total_characters -- contains the total characters
          within self.file_path's file.

        Return:
          int file_total_characters -- total character count
        '''
        file_total_characters = 0
        try:
            with open(self.file_path, "r") as file: # type: ignore
                file_content = file.read()
                file_total_characters = len(file_content)
        except FileNotFoundError:
            print("The current file could not be found or isn't readable!")
        return file_total_characters

    def total_file_size(self) -> int:
        '''
        Function that uses pandas to get the current file_path's
        file size.

        Variables:
          str file_path -- str that holds the current file
          int file_size -- int that holds the current file's
          filesize in bytes.

        Return:
          int file_size -- total self.file_path's size in bytes
        '''
        file_size = 0
        try:
            file_path = pb.Path(self.file_path) # type: ignore
            file_size = file_path.stat().st_size
        except FileNotFoundError:
            print("The current file could not be found or isn't readable!")
        return file_size

if __name__ == '__main__':
    test = Text_File()
    test.set_filepath("sample.txt")
    lines = test.total_lines()
    file_size = test.total_file_size()
    characters = test.total_characters()
    print("Total lines with line-breaks:", lines[0])
    print("Total lines without line-breaks:", lines[1])
    print("Total file-size:", file_size, "Bytes")
    print("Current file path:", test.get_filepath())
    print("Current file extension type:", test.get_file_extension())
    print("Total characters:", characters)
    input("Press ENTER to continue...")
