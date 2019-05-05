import os
from contextlib import contextmanager

##### Good with files, databases,locks etc.####

# """ Common example is with  files"""
# # Old way
# f = open('sample .txt', 'w')
# f.write('Hi there, there is a better way to work with files - see below')
# f.close()
#
# # Better way using context managers - automatically close file if error
# with open('sample.txt', 'w') as f:
#     f.write('This is a better way of working with files.')

#### using a class to create context manager
# class Open_File():
#
#     def __init__(self, filename, mode):
#         self.filename = filename
#         self.mode = mode
#
#     def __enter__(self):
#         self.file = open(self.filename, self.mode)
#         return self.file
#
#     def __exit__(self, exc_type, exc_val, traceback):
#         self.file.close()


#### Using contextlib - function ####

# @contextmanager
# def open_file(file, mode):
#     f = open(file, mode)    # equivalent of init
#     yield f                 # equivalent of __enter__
#     f.close()               # equivalent of __exit__
#
#
# with open_file('sample.txt', 'w') as f:
#     f.write('Lorem ipsum dolor sit amet, consectetur adipiscing elit.')
#
# print(f.closed)


#### CD Example ####
# # Without context manager
# cwd = os.getcwd()
# os.chdir('TKINTER')
# print(os.listdir())
# os.chdir(cwd)
#
# cwd = os.getcwd()
# os.chdir('SQLite')
# print(os.listdir())
# os.chdir(cwd)

@contextmanager
def change_dir(destination):
    try:
        cwd = os.getcwd()   # Setup
        os.chdir(destination)
        yield
    finally:
        os.chdir(cwd)   # Teardown


with change_dir('TKINTER'):
    print(os.listdir())

with change_dir('SQLite'):
    print(os.listdir())
