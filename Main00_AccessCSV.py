# CSV with different cols
import os
from os import walk
import glob
from numpy import genfromtxt
import numpy
import csv
import pickle

FileDirectoryPath = 'H:/netData/DynamicModel/jrvicon'
# files=[]

files = [f for f in sorted(os.listdir(FileDirectoryPath))]
print(files)
my_data = {'sample': 2}
for num, name in enumerate(files, start=1):
    pngpath = os.path.join(FileDirectoryPath, name)
    print(pngpath)
    my_data[name] = genfromtxt(pngpath, delimiter=',', skip_header = 3)

print(my_data.get('Act11_Ver7_Exp11_180913_1710.csv'))

