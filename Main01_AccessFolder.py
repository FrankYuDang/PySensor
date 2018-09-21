import os
from numpy import genfromtxt
import pickle


RawDataFolder = 'H:/netData/DynamicModel/jrvicon'
# SaveDataFolder = os.path.join('H:/netData/DynamicModel/jrvicon_data', 'my_data.pkl')
SaveDataName = RawDataFolder.split('/')[3] + '.pkl'
SaveDataFolder = os.path.join('H:/netData/DynamicModel/jrvicon_data', SaveDataName)
CSVSkipRows = 14
TestName = [f for f in sorted(os.listdir(RawDataFolder))]
print(TestName)

# Access to the data
test_data = {'header': RawDataFolder}
for num, name in enumerate(TestName, start=1):
    TestRawDataPath = os.path.join(RawDataFolder, name)
    # print(pngpath)
    test_data[name] = genfromtxt(TestRawDataPath, delimiter=',', skip_header = CSVSkipRows)

# Store data
with open(SaveDataFolder, 'wb') as f:
    # Pickle the dictionary using the highest protocol available
    pickle.dump(test_data, f, pickle.HIGHEST_PROTOCOL)
