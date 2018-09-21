# Created - Sept 21, This script is used for creating the pkl of each test setsetting.

# Put Data into the same categories.
import os
import pickle
import scipy.signal
# focus on one situation:
TestSetting = 'R25T30'
k = 3 # the valid data order 1 2 3

# load raw data
LoadGroupedDataFolder = os.path.join('H:/netData/DynamicModel/jrvicon_data', 'GroupedData.pkl')

with open(LoadGroupedDataFolder, 'rb') as f:
    savedData = pickle.load(f)
TestName = [f for f in savedData.keys()]

TestResults ={ TestSetting: "data"}

for num, name in enumerate(TestName, start= 1):
    if name.find(TestSetting) == -1:
        print(name)
    else:
        print('Yes')
        TestResults.update({name:savedData.get(name)})
        print(TestResults.keys())
# focus on one tests
TestResultsName = [f for f in TestResults.keys()]
TestResultsValue =  TestResults.get(TestResultsName[k])

TimeStamp = TestResultsName[k].split('_')[1]
SaveOneTestSetting = TestSetting + 'GroupedData' + TimeStamp + '.pkl'
SaveOneSettingDataFolder = os.path.join('H:/netData/DynamicModel/jrvicon_data',SaveOneTestSetting )
# Separate the data.
marker1 = TestResultsValue[:,0:3]
ref1 = TestResultsValue[:,3:6]
ref2 = TestResultsValue[:,6:9]
ref3 = TestResultsValue[:,9:12]
ref4 = TestResultsValue[:,12:15]
r1Delta = TestResultsValue[:,15]
r2Delta = TestResultsValue[:,16]
r3Delta = TestResultsValue[:,17]
FeedForwardP = TestResultsValue[:,18]
MeasuredSmoothP = TestResultsValue[:,19]
size = 21
PrescribeCtrRa = scipy.signal.medfilt(TestResultsValue[:,20], size)
GroupedData = {'marker1':marker1,'ref1':ref1,'ref2':ref2, 'ref3':ref3, 'ref4':ref4}
GroupedData.update({'r1Delta' : r1Delta, 'r2Delta': r2Delta, 'r3Delta': r3Delta })
GroupedData.update({'FeedForwardP' : FeedForwardP, 'MeasuredSmoothP': MeasuredSmoothP, 'PrescribeCtrRa': PrescribeCtrRa })

# Store data
with open(SaveOneSettingDataFolder, 'wb') as f:
    # Pickle the dictionary using the highest protocol available
    pickle.dump(GroupedData, f, pickle.HIGHEST_PROTOCOL)

