import os


def directInfo(direct=None):
    if direct == None:
        return os.listdir()
    else:
        os.chdir(direct)
        return os.listdir()


print(directInfo())
print(directInfo('C:\Program Files (x86)'))
