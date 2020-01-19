
def read_file(file_path : str, is_generator : bool = False):
    with open (file_path, 'r') as f:
        line_num = 1
        while line := f.readline():
            #print(line_num)
            #line_num += 1
            yield int(line)
