#info_file = r"C:\Users\Guest1\Desktop\test.txt"
info_file = r"C:\Users\Guest1\Desktop\code\PythonZTM\info.txt"

def read_file():
    f = open(info_file, 'r')
    print(f) # Prints the file object
    print(f.read()) # Prints the content of the file
    f.close()

def write_file(text):
    f = open(info_file, 'w')
    f.write(text + '\n') 
    f.close()

def append_file(text):
    f = open(info_file, 'a')
    f.write(text + '\n')
    
    f.close()

def read_file_one_line():
    f = open(info_file, 'r')
    print(f.readline())
    f.close()

def read_file_all_lines():
    f = open(info_file, 'r')
    print(f.readlines())
    f.close()

def read_file_all_lines_loop():
    f = open(info_file, 'r')
    for line in f:
        print(line)
    f.close()

read_file() # Hi
write_file("This is a test file")   # This is a test file
append_file("Appending the file")   # This is a test fileAppending the file
read_file()                         # This is a test file. Appending the file