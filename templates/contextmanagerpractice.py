#context manager
#no need to close file and  if there is error
#in execution then also file will be closed successfully
#context manager is used for opening and closing database

'''with open('sample.txt','w') as f:
    f.write('just for example')
'''
import os
from contextlib import contextmanager

'''class Open_file():
    def __init__(self,filename,mode):
        self.filename=filename
        self.mode=mode
    def __enter__(self):
        self.file=open(self.filename,self.mode)
        return self.file
    def __exit__(self, exc_type, exc_val, traceback):
        self.file.close()

with Open_file('sample.txt','w') as f:
    f.write('Testing')

print(f.closed)
'''

'''@contextmanager
def open_file(file,mode):
    f=open(file,mode)
    yield f
    f.close()
with open_file('sample.txt','w') as f:
    f.write('my name is aman')

print(f.closed)
'''

cwd=os.getcwd()
os.chdir('Sample-Dir-One')
print(os.listdir())
os.chdir(cwd)

cwd=os.getcwd()
os.chdir('Sample-Dir-Two')
print(os.listdir())
os.chdir(cwd)


#another way to do it
@contextmanager
def change_dir(destination):
    try:
        cwd=os.getcwd()
        os.chdir(destination)
        yield
    finally:
        os.chdir(cwd)
with change_dir('Sample-Dir-One'):
    print(os.listdir())








