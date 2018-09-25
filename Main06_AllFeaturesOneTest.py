import pickle
import os
import numpy as np
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt
import myFunc


# Load Related Data
test1 = os.path.join('H:/netData/DynamicModel/jrvicon_data', 'R25T30GroupedData1809131632PoseInfo.pkl')
test2 = os.path.join('H:/netData/DynamicModel/jrvicon_data', 'R25T30GroupedData1809131636PoseInfo.pkl')
test3 = os.path.join('H:/netData/DynamicModel/jrvicon_data', 'R25T30GroupedData1809131642PoseInfo.pkl')
testNo = [test1, test2, test3]
k = 3 # 1 2 3
with open(test1, 'rb') as f:
    test1Data = pickle.load(f)
with open(test2, 'rb') as f:
    test2Data = pickle.load(f)
with open(test3, 'rb') as f:
    test3Data = pickle.load(f)

timestamp = myFunc.timestamp(testNo[k-1])
TestSetting = myFunc.testsetting(testNo[k-1])
testDataProcess = [test1Data, test2Data, test3Data]
print('test is processing {} {}'.format(TestSetting, timestamp))
### Create teh interpolation function
# Load the theoretical results for prediction and comparison.
with open('shapeTablePy.pkl', 'rb') as f:
    shapeTable = pickle.load(f)
# Interpolate the predication based on the measured data.
pressure = shapeTable.get('pressure')[4:23]/1000
ContractionRatio = shapeTable.get('ContractionRatio')[4:23]
StretchRatio = shapeTable.get('StretchRatio')[4:23]
# Construct the mapping among Pressure and Deforamation
func_P2CR = interp1d(pressure, ContractionRatio, fill_value='extrapolate' )
func_P2SR = interp1d(pressure, StretchRatio)
func_CR2P = interp1d( ContractionRatio, pressure)
func_SR2P = interp1d( StretchRatio, pressure)
### Analysis the data
test1M1 = test1Data[1].get('marker1Info')
test2M1 = test2Data[1].get('marker1Info')
test3M1 = test3Data[1].get('marker1Info')

testToProcess = testDataProcess[k-1][1].get('marker1Info')

#
# # Clear peculiar data
# aa = testToProcess.get('CRatio')
# bb = np.where(aa>1)
# print('the index of peculiar pt in CRatio: {}'.format(bb))
# aa[bb[0][0]] = aa[bb[0][0] - 1]
# aa[bb[0][1]] = aa[bb[0][1] - 1]
#
#
# aa = testToProcess.get('RadialTransPos')
# bb = np.where(aa>60)
# print('the index of peculiar pt in RadialTransPos: {}'.format(bb))
# aa[bb[0][0]] = aa[bb[0][0] - 1]
# aa[bb[0][1]] = aa[bb[0][1] - 1]


time = np.arange(len(testToProcess.get('raw')))*0.05
time = time[400: -400]
print('Time length is {}'.format(len(time)))
# Pressure info
p_fig, p_ax = plt.subplots()
p_ax.plot(time, testToProcess.get('MeasuredSmoothP')[400: -400], '.b')
p_ax.legend(['MeasuredSmoothP'])
title = 'MeasuredSmoothP' + TestSetting + timestamp
p_ax.set_title(title)
p_ax.set_ylabel('Pressure (kPa)')
p_ax.set_xlabel('Time (Sec)')
p_fig.savefig(title + ".png")
# Resistance info
R_fig, R_ax = plt.subplots()
R_ax.plot(time, testToProcess.get('Resistance1')[400: -400], '.b')
R_ax.legend(['Resistance1'])
title = 'Resistance1' + TestSetting + timestamp
R_ax.set_title(title)
R_ax.set_xlabel('Time (Sec)')
R_ax.set_ylabel('Resistance (k$\Omega$)')
R_fig.savefig(title + ".png")
# CRatio info
CRatio_fig, CRatio_ax = plt.subplots()
CRatio_ax.plot(time, testToProcess.get('CRatio')[400: -400], '.b')
CRatio_ax.legend(['CRatio'])
title = 'CRatio' + TestSetting + timestamp
CRatio_ax.set_title(title)
CRatio_ax.set_xlabel('Time (Sec)')
CRatio_ax.set_ylabel('Contract Ratio')
CRatio_fig.savefig(title + ".png")

# RadialTransPos info
RadialTransPos_fig, RadialTransPos_ax = plt.subplots()
RadialTransPos_ax.plot(time, testToProcess.get('RadialTransPos')[400: -400], '.b')
RadialTransPos_ax.legend(['RadialTransPos'])
title = 'RadialTransPos' + TestSetting + timestamp
RadialTransPos_ax.set_title(title)
RadialTransPos_ax.set_xlabel('Time (Sec)')
RadialTransPos_ax.set_ylabel('RadialTransPos (mm)')
RadialTransPos_fig.savefig(title + ".png")

OriginalTestName = testNo[k-1]
timestampA = myFunc.timestamp(OriginalTestName)
TestSettingA = myFunc.testsetting(OriginalTestName)
DataTitle = TestSettingA + 'TestInfo' + timestampA
DataTitle.strip('PoseInfo')
testData = {'time' : time, 'pressure' : testToProcess.get('MeasuredSmoothP')[400: -400]}
testData.update({'resistance' : testToProcess.get('Resistance1')[400: -400],
                 'CRatio' : testToProcess.get('CRatio')[400: -400],
                 'RadialTrans': testToProcess.get('RadialTransPos')[400: -400],
                 'PrescribedCtrRa': testToProcess.get('PrescribeCtrRa')[400: -400]})

savefilename = DataTitle.strip('PoseInfo') + '.pkl'
SaveFolder = os.path.join('H:/netData/DynamicModel/jrvicon_data', savefilename)
print('New Data file name is {}'.format(savefilename))
with open(SaveFolder, 'wb') as f:
    # Pickle the dictionary using the highest protocol available
    pickle.dump(testData, f, pickle.HIGHEST_PROTOCOL)

# Compare with each other
PreCtrRa2MeasCtrRa_fig, PreCtrRa2MeasCtrRa_ax = plt.subplots()
# p_fig, p_ax = plt.subplots()
PreCtrRa2MeasCtrRa_ax.plot(time, testToProcess.get('PrescribeCtrRa')[400: -400], '.b')
PreCtrRa2MeasCtrRa_ax.plot(time, testToProcess.get('CRatio')[400: -400], '.r')

PreCtrRa2MeasCtrRa_ax.legend(['PrescribeCtrRa', 'CRatio'])
title = 'PrescribeCtrRa' + TestSetting + timestamp
PreCtrRa2MeasCtrRa_ax.set_title(title)
PreCtrRa2MeasCtrRa_ax.set_ylabel('Ratio($\Lambda_1$)')
PreCtrRa2MeasCtrRa_ax.set_xlabel('Time (Sec)')
PreCtrRa2MeasCtrRa_fig.savefig(title + ".png")
