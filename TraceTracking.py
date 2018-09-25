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
func_CR2P = interp1d( ContractionRatio, pressure, fill_value='extrapolate')
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
# Compare with each other In terms of Contraction Ratio
PreCtrRa2MeasCtrRa_fig, PreCtrRa2MeasCtrRa_ax = plt.subplots()
# p_fig, p_ax = plt.subplots()
PreCtrRa2MeasCtrRa_ax.plot(time, testToProcess.get('PrescribeCtrRa')[400: -400], '.b')
PreCtrRa2MeasCtrRa_ax.plot(time, testToProcess.get('CRatio')[400: -400], '.r')

PreCtrRa2MeasCtrRa_ax.legend(['PrescribeCtrRa', 'CRatio'])
# title = 'PrescribeCtrRa' + TestSetting + timestamp
title = 'Contraction Comparison'
PreCtrRa2MeasCtrRa_ax.set_title(title)
PreCtrRa2MeasCtrRa_ax.set_ylabel('Ratio($\Lambda_1$)')
PreCtrRa2MeasCtrRa_ax.set_xlabel('Time (Sec)')
PreCtrRa2MeasCtrRa_fig.savefig(title + ".png")

# Compare with each other In terms of pressure value
PrePressure2MeasPressure_fig, PrePressure2MeasPressure_ax = plt.subplots()
# p_fig, p_ax = plt.subplots()
PrePressure2MeasPressure_ax.plot(time, func_CR2P(testToProcess.get('CRatio')[400: -400]), '.b')
PrePressure2MeasPressure_ax.plot(time, testToProcess.get('MeasuredSmoothP')[400: -400], '.r')

PrePressure2MeasPressure_ax.legend(['Prescribe Pressure', 'measured pressure'])
# title = 'Pressure Comparison' + TestSetting + timestamp
title = 'Pressure Comparison'
PrePressure2MeasPressure_ax.set_title(title)
PrePressure2MeasPressure_ax.set_ylabel('Pressure [kPa]')
PrePressure2MeasPressure_ax.set_xlabel('Time (Sec)')
PrePressure2MeasPressure_fig.savefig(title + ".png")
