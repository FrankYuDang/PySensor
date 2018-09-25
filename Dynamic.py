# CSV with different cols
import os
from os import walk
import glob
from numpy import genfromtxt
import matplotlib.pyplot as plt
from matplotlib import rc
import numpy as np
from pandas import rolling_mean
import csv
import pickle

### Running mean/Moving average
def running_mean(l, N):
    sum = 0
    result = list( 0 for x in l)

    for i in range( 0, N ):
        sum = sum + l[i]
        result[i] = sum / (i+1)

    for i in range( N, len(l) ):
        sum = sum - l[i-N] + l[i]
        result[i] = sum / N

    return result

# How to push in the Github
FileDirectoryPath = 'H:/netData\DynamicModel\July09_dynamic\RawData\pyData'

files = [f for f in sorted(os.listdir(FileDirectoryPath))]
print(files)
my_data = {'sample': 2}
for num, name in enumerate(files, start=1):
    pngpath = os.path.join(FileDirectoryPath, name)
    print(pngpath)
    my_data[name] = genfromtxt(pngpath, delimiter=',', skip_header = 3)

print(my_data.get('Act11_Ver5_Exp11_180913_1710.csv'))
measured_pressure = my_data.get('Act4_Ver4_Exp5_180709_1135.csv')[:,0]
desired_pressure = my_data.get('Act4_Ver4_Exp5_180709_1135.csv')[:,1]

# Figure setting
rc('font',**{'family':'serif','serif':['Times']})
rc('text', usetex=True)
plt.rcParams["font.family"] = "Times New Roman"
plt.rc('xtick', labelsize=8)
plt.rc('ytick', labelsize=8)
plt.rc('axes', labelsize=8)

# width as measured in inkscape
width = 3.4
height = width / 1.618
p_fig, p_ax = plt.subplots()
# set the edges of the subplots of the figure.
plt.subplots_adjust(left=.15, bottom=.20, right=.95, top=.95)
time = np.arange(len(desired_pressure)) * 0.05
p_ax.plot(time, desired_pressure, '-r')
p_ax.plot(time, running_mean( measured_pressure, 50), '-b')
p_ax.set_xlabel('Time [Sec]')
p_ax.set_ylabel('Pressure [kPa]')
p_ax.legend(['Desired Pressure (kPa)', 'Measured Pressure (kPa)'])
# ax.legend(ln1.get_label())
p_fig.set_size_inches(width, height)
plt.savefig('Dynamics Slope.pdf')
p_fig.show()



