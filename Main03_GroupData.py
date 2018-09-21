# Put Data into the same categories.
import os
import pickle
from numpy import genfromtxt
# load raw data

RawDataFolder = os.path.join('H:/netData/DynamicModel/jrvicon_data', 'jrvicon.pkl')
SaveGroupedDataFolder = os.path.join('H:/netData/DynamicModel/jrvicon_data', 'GroupedData.pkl')
with open(RawDataFolder, 'rb') as f:
    savedData = pickle.load(f)
TestName = [f for f in savedData.keys()]
# print(TestName)
naming_dict = {'Exp1': 'R20T10_', 'Exp2': 'R20T10_', 'Exp3': 'R20T10_'}
naming_dict.update({'Exp4': 'R25T10_', 'Exp5': 'R25T10_', 'Exp6': 'R25T10_'})
naming_dict.update({'Exp7': 'R30T10_', 'Exp8': 'R30T10_', 'Exp9': 'R30T10_'})

naming_dict.update({'Exp10': 'R20T20_', 'Exp11': 'R20T20_', 'Exp12': 'R20T20_'})
naming_dict.update({'Exp13': 'R25T20_', 'Exp14': 'R25T20_', 'Exp15': 'R25T20_'})
naming_dict.update({'Exp16': 'R30T20_', 'Exp17': 'R30T20_', 'Exp18': 'R30T20_'})

naming_dict.update({'Exp19': 'R20T30_', 'Exp20': 'R20T30_', 'Exp21': 'R20T30_'})
naming_dict.update({'Exp22': 'R25T30_', 'Exp23': 'R25T30_', 'Exp24': 'R25T30_'})
naming_dict.update({'Exp25': 'R30T30_', 'Exp26': 'R30T30_', 'Exp27': 'R30T30_'})

GroupData = {'TestGroup': RawDataFolder}
for TestNameRawKey in TestName[1:]:
    print(TestNameRawKey)
    # TestNameRawKey = TestName[1]
    bb = TestNameRawKey.strip('.csv')
    splitTestName = bb.split('_')
    TimeTag = splitTestName[-2] + splitTestName[-1]
    TestGroup = naming_dict.get(splitTestName[2]) + TimeTag
    print(TestGroup)
    GroupData.update({TestGroup : savedData.get(TestNameRawKey)})
    print(TestNameRawKey)
## Sort data group the data into same categories to do computing


with open(SaveGroupedDataFolder, 'wb') as f:
    # Pickle the dictionary using the highest protocol available
    pickle.dump(GroupData, f, pickle.HIGHEST_PROTOCOL)
