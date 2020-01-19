import re

def get_file_path(day):
    return f'inputfiles\\day{day}.txt'

def read_file_lines(file_path : str) -> int:
    with open (file_path, 'r') as f:
        while line := f.readline():
            yield int(line)

def read_file_delimited(file_path : str, delimeters : list) -> list:
    """[summary]
    Yields each line as a list of strings
    
    Arguments:
        file_path {str} -- Path to the file
        delimeters {list} -- List of delimeters we split the line on
    
    Yields:
        list -- [description]
    """
    pattern = '|'.join(map(re.escape, delimeters))
    with open(file_path, 'r') as f:
        while line := f.readline():
            yield list(map(int, re.split(pattern, line)))

        
