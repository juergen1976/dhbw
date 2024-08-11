class FileReader:
    def __init__(self, filename):
        self.filename = filename
        self.file = open(filename, 'r')

    def __iter__(self):
        return self

    def __next__(self):
        line = self.file.readline()
        if not line:
            self.file.close()
            raise StopIteration()
        return line.strip()

my_file_reader = FileReader('example.txt')
for line in my_file_reader:
    print(line)