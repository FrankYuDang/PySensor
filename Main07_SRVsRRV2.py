import pickle
import os
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt
import myFunc
import numpy as np
import scipy.io as spio
import datetime
# Load Related Data
test1 = os.path.join('H:/netData/DynamicModel/jrvicon_data', 'R25T30TestInfo1809131632.pkl')
test2 = os.path.join('H:/netData/DynamicModel/jrvicon_data', 'R25T30TestInfo1809131636.pkl')
test3 = os.path.join('H:/netData/DynamicModel/jrvicon_data', 'R25T30TestInfo1809131642.pkl')
testNo = [test1, test2, test3]
k = 1 # 1 2 3
with open(test1, 'rb') as f:
    test1Data = pickle.load(f)
with open(test2, 'rb') as f:
    test2Data = pickle.load(f)
with open(test3, 'rb') as f:
    test3Data = pickle.load(f)
timestamp1 = myFunc.timestamp(test1)
TestSetting1 = myFunc.testsetting(test1)
testDataProcess = [test1Data, test2Data, test3Data]

##########################################################################
##  Create teh interpolation function
# Load the theoretical results for prediction and comparison.
with open('shapeTablePy.pkl', 'rb') as f:
    shapeTable = pickle.load(f)

### This part is for referring to the Shape and build the functions
# Interpolate the predication based on the measured data.
pressure = shapeTable.get('pressure')[4:23]/1000
ContractionRatio = shapeTable.get('ContractionRatio')[4:23]
StretchRatio = shapeTable.get('StretchRatio')[4:23]

CrSr_fig, CrSr_ax = plt.subplots()
CrSr_ax.plot(ContractionRatio, StretchRatio)
CrSr_ax.set_xlabel('ContractionRatio')
CrSr_ax.set_ylabel('StretchRatio')
CrSr_fig.show()
# Construct the mapping among Pressure and Deforamation
func_P2CR = interp1d(pressure, ContractionRatio)
func_P2SR = interp1d(pressure, StretchRatio)

func_CR2P = interp1d( ContractionRatio, pressure)
func_SR2P = interp1d( StretchRatio, pressure)

func_CR2SR = interp1d( ContractionRatio, StretchRatio, fill_value='extrapolate')
######################################################################
# testToProcess1 = testDataProcess[k-2]
# testToProcess3 = testDataProcess[k-1]
# testToProcess2 = testDataProcess[k]
testToProcess1 = test1Data
testToProcess2 = test2Data
testToProcess3 = test3Data

# Whole Graphs: Stretch Ratio Vs. Resistance Raw Data
SR2R_fig, SR2R_ax = plt.subplots()
SR2R_ax.plot(func_CR2SR(testToProcess1.get('CRatio')), testToProcess1.get('resistance'), '.r')
SR2R_ax.plot(func_CR2SR(testToProcess2.get('CRatio')), testToProcess2.get('resistance'), '.y')
SR2R_ax.plot(func_CR2SR(testToProcess3.get('CRatio')), testToProcess3.get('resistance'), '.c')
SR2R_ax.legend(['test1 data', 'test2 data','test3 data'])
now = datetime.datetime.now()
title = 'SR2R' + now.strftime("_%b%d_%I%M") + '.png'
# title = 'SR2R' + TestSetting
SR2R_ax.set_title(title)
SR2R_ax.set_xlabel('Contraction Ratio')
SR2R_ax.set_ylabel('Resistance (k$\Omega$)')
# p2d_fig.savefig(title + ".png")
SR2R_fig.show()

# The whole graph describing Pressure Vs. Contraction Ratio
P2CRatio_fig, P2CRatio_ax = plt.subplots()
P2CRatio_ax.plot(testToProcess1.get('pressure'), testToProcess1.get('CRatio'), '.r', alpha=0.5)
P2CRatio_ax.plot(testToProcess2.get('pressure'), testToProcess2.get('CRatio'), '.y', alpha=0.4)
P2CRatio_ax.plot(testToProcess3.get('pressure'), testToProcess3.get('CRatio'), '.c', alpha=0.3)
P2CRatio_ax.plot(testToProcess3.get('pressure'), func_P2CR(testToProcess3.get('pressure')), '.b')
P2CRatio_ax.legend(['test1 data', 'test2 data','test3 data', 'Prediction'])
title = 'Pressure vs CtrRatio'
P2CRatio_ax.set_title(title)
P2CRatio_fig.savefig(title + TestSetting +  ".png")
P2CRatio_fig.show()

# title = 't2R' + TestSetting
# t2R_ax.set_title(title)
# t2R_fig.savefig(title + ".png")
# t2R_fig.show()


# t2R_fig
# The pressure, as a function of time.
t2p_fig, t2p_ax = plt.subplots()
t2p_ax.plot(testToProcess1.get('time'), testToProcess1.get('pressure'), '.r')
t2p_ax.plot(testToProcess2.get('time'), testToProcess2.get('pressure'), '.y')
t2p_ax.plot(testToProcess3.get('time'), testToProcess3.get('pressure'), '.c')
t2p_ax.legend(['test1 Data', 'test2 data','test3 data'])
title = 't2p' + TestSetting
t2p_ax.set_title(title)
# p2d_fig.savefig(title + ".png")
t2p_fig.show()

# The resistance, as a function of time.
t2R_fig, t2R_ax = plt.subplots()
t2R_ax.plot(testToProcess1.get('time'), testToProcess1.get('resistance'), '.r')
t2R_ax.plot(testToProcess2.get('time'), testToProcess2.get('resistance'), '.y')
t2R_ax.plot(testToProcess3.get('time'), testToProcess3.get('resistance'), '.c')
t2R_ax.legend(['test1 Data', 'test2 data','test3 data'])
title = 't2R' + TestSetting
t2R_ax.set_title(title)
t2R_fig.savefig(title + ".png")
t2R_fig.show()

# Precribed contraction, a function of time, this serving for locating the time sequence.
t2Prescribed_fig, t2Prescribed_ax = plt.subplots()
t2Prescribed_ax.plot(testToProcess1.get('time'), testToProcess1.get('PrescribedCtrRa'), '.r')
t2Prescribed_ax.plot(testToProcess2.get('time'), testToProcess2.get('PrescribedCtrRa'), '.y')
t2Prescribed_ax.plot(testToProcess3.get('time'), testToProcess3.get('PrescribedCtrRa'), '.c')
t2Prescribed_ax.legend(['test1 Data', 'test2 data','test3 data'])
title = 't2PrescribedCtrRa' + TestSetting
t2Prescribed_ax.set_title(title)
t2Prescribed_fig.savefig(title + ".png")
t2Prescribed_fig.show()

#############################################################
# Calculate the different points and slice the signals
# the ramp up phase. and ramp down phase.

t2diff_fig, t2diff_ax = plt.subplots()
t2diff_ax.plot(testToProcess1.get('time')[:-1], np.diff(testToProcess1.get('PrescribedCtrRa')), '.r')
t2diff_ax.legend(['test1 Data'])
title = 't2diff' + TestSetting
t2diff_ax.set_title(title)
# p2d_fig.savefig(title + ".png")
t2diff_fig.show()

TimeSequenceMarker = np.diff(testToProcess1.get('PrescribedCtrRa'))
TimeRise = np.where(TimeSequenceMarker == TimeSequenceMarker.max())[0]
RiseSplit = np.where( np.diff(TimeRise) > 20)[0]
TimeRisePhaseIndex = np.array( [TimeRise[0], TimeRise[RiseSplit], TimeRise[RiseSplit+1], TimeRise[-1]] )

TimeDown = np.where(TimeSequenceMarker == TimeSequenceMarker.min())[0]
DownSplit = np.where( np.diff(TimeDown) > 20)[0]
TimeDownPhaseIndex = np.array( [TimeDown[0], TimeDown[DownSplit], TimeDown[DownSplit+1], TimeDown[-1]] )

# Drawing the 3D graphs. 
fig = plt.figure()
ax = fig.gca(projection='3d')
x1 = testToProcess1.get('resistance')[TimeRisePhaseIndex[0]:TimeRisePhaseIndex[1]]
y1 = testToProcess1.get('PrescribedCtrRa')[TimeRisePhaseIndex[0]:TimeRisePhaseIndex[1]]
z1 = testToProcess1.get('time')[TimeRisePhaseIndex[0]:TimeRisePhaseIndex[1]]
x2 = testToProcess2.get('resistance')[TimeRisePhaseIndex[0]:TimeRisePhaseIndex[1]]
y2 = testToProcess2.get('PrescribedCtrRa')[TimeRisePhaseIndex[0]:TimeRisePhaseIndex[1]]
z2 = testToProcess2.get('time')[TimeRisePhaseIndex[0]:TimeRisePhaseIndex[1]]
x3 = testToProcess3.get('resistance')[TimeRisePhaseIndex[0]:TimeRisePhaseIndex[1]]
y3 = testToProcess3.get('PrescribedCtrRa')[TimeRisePhaseIndex[0]:TimeRisePhaseIndex[1]]
z3 = testToProcess3.get('time')[TimeRisePhaseIndex[0]:TimeRisePhaseIndex[1]]
ax.set_xlabel('Resistance')
ax.set_ylabel('RescribedCtrRa')
ax.set_zlabel('Time')
ln1 = ax.plot(x1, y1, z1, '.r', label='test1' )
ln2 = ax.plot(x2, y2, z2, '.b', label='test2')
ln3 = ax.plot(x3, y3, z3, '.m', label='test3')
# added these three lines
lns = ln1+ln2+ln3
labs = [l.get_label() for l in lns]
ax.legend(lns, labs, loc=0)
ax.legend()
now = datetime.datetime.now()
title = 'Resistance' + 'PreCtrRa' + 'Time'+ now.strftime("_%b%d_%I%M")
# ax.title(title)
fig.savefig(title + '.png')
plt.show()

#############################################################################################################
# When we only focus on the single ramp up and part of it.
# Pressure to Resistance Ratio
# Compute it in a differnt way ..
p2r_fig, p2r_ax = plt.subplots()
lns1 = p2r_ax.plot(testToProcess1.get('pressure')[TimeRisePhaseIndex[0]:TimeRisePhaseIndex[1]],
            testToProcess1.get('resistance')[TimeRisePhaseIndex[0]:TimeRisePhaseIndex[1]]/testToProcess1.get('resistance')[TimeRisePhaseIndex[0]]
            , '.b', label = 'test 1 - up1')
lns2 = p2r_ax.plot(testToProcess1.get('pressure')[TimeDownPhaseIndex[2]:TimeDownPhaseIndex[3]],
           testToProcess1.get('resistance')[TimeDownPhaseIndex[2]:TimeDownPhaseIndex[3]]/testToProcess1.get('resistance')[TimeDownPhaseIndex[2]]
            , '.c', label = 'test 1 - up2')
lns3 = p2r_ax.plot(testToProcess2.get('pressure')[TimeRisePhaseIndex[0]:TimeRisePhaseIndex[1]],
            testToProcess2.get('resistance')[TimeRisePhaseIndex[0]:TimeRisePhaseIndex[1]]/testToProcess2.get('resistance')[TimeRisePhaseIndex[0]]
            , '.r', label = 'test 2 - up1')
lns4 = p2r_ax.plot(testToProcess2.get('pressure')[TimeDownPhaseIndex[2]:TimeDownPhaseIndex[3]],
        testToProcess2.get('resistance')[TimeDownPhaseIndex[2]:TimeDownPhaseIndex[3]]/testToProcess2.get('resistance')[TimeDownPhaseIndex[2]]
            , '.k', label = 'test 2 - up2')

lns5 = p2r_ax.plot(testToProcess3.get('pressure')[TimeRisePhaseIndex[0]:TimeRisePhaseIndex[1]],
            testToProcess3.get('resistance')[TimeRisePhaseIndex[0]:TimeRisePhaseIndex[1]]/testToProcess3.get('resistance')[TimeRisePhaseIndex[0]]
            , '.y', label = 'test 3 - up1')
lns6 = p2r_ax.plot(testToProcess2.get('pressure')[TimeDownPhaseIndex[2]:TimeDownPhaseIndex[3]],
        testToProcess3.get('resistance')[TimeDownPhaseIndex[2]:TimeDownPhaseIndex[3]]/testToProcess3.get('resistance')[TimeDownPhaseIndex[2]]
            , '.m', label = 'test 3 - up2')
# x label and y label
p2r_ax.set_xlabel('Pressure (kPa)')
p2r_ax.set_ylabel('Resistance Ratio')
# added these three lines
lns = lns1+lns2+lns3 + lns4+lns5+lns6
labs = [l.get_label() for l in lns]
p2r_ax.legend(lns, labs, loc=0)
# demo_ax.legend('Test Demo')
now = datetime.datetime.now()
title = 'p2r_fig' + now.strftime("_%b%d_%I%M") + '.png'
plt.savefig(title)
p2r_fig.show()

#############################################################################################################
# When we only focus on the single ramp up and part of it.
# Contraction Ratio Vs Resistance Ratio
CRatio2ResisRatio_fig, CRatio2ResisRatio_ax = plt.subplots()
lns1 = CRatio2ResisRatio_ax.plot(testToProcess1.get('CRatio')[TimeRisePhaseIndex[0]:TimeRisePhaseIndex[1]],
            testToProcess1.get('resistance')[TimeRisePhaseIndex[0]:TimeRisePhaseIndex[1]] / testToProcess1.get('resistance')[TimeRisePhaseIndex[0]]
                                 , '.b', label = 'test 1 - up1')
lns2 = CRatio2ResisRatio_ax.plot(testToProcess1.get('CRatio')[TimeDownPhaseIndex[2]:TimeDownPhaseIndex[3]],
        testToProcess1.get('resistance')[TimeDownPhaseIndex[2]:TimeDownPhaseIndex[3]] / testToProcess1.get('resistance')[TimeDownPhaseIndex[2]]
                                 , '.c', label = 'test 1 - up2')

lns3 = CRatio2ResisRatio_ax.plot(testToProcess2.get('CRatio')[TimeRisePhaseIndex[0]:TimeRisePhaseIndex[1]],
            testToProcess2.get('resistance')[TimeRisePhaseIndex[0]:TimeRisePhaseIndex[1]] / testToProcess2.get('resistance')[TimeRisePhaseIndex[0]]
                                 , '.r', label = 'test 2 - up1')
lns4 = CRatio2ResisRatio_ax.plot(testToProcess2.get('CRatio')[TimeDownPhaseIndex[2]:TimeDownPhaseIndex[3]],
        testToProcess2.get('resistance')[TimeDownPhaseIndex[2]:TimeDownPhaseIndex[3]] / testToProcess2.get('resistance')[TimeDownPhaseIndex[2]]
                                 , '.k', label = 'test 2 - up2')

lns5 = CRatio2ResisRatio_ax.plot(testToProcess3.get('CRatio')[TimeRisePhaseIndex[0]:TimeRisePhaseIndex[1]],
            testToProcess3.get('resistance')[TimeRisePhaseIndex[0]:TimeRisePhaseIndex[1]] / testToProcess3.get('resistance')[TimeRisePhaseIndex[0]]
                                 , '.y', label = 'test 3 - up1')
lns6 = CRatio2ResisRatio_ax.plot(testToProcess2.get('CRatio')[TimeDownPhaseIndex[2]:TimeDownPhaseIndex[3]],
        testToProcess3.get('resistance')[TimeDownPhaseIndex[2]:TimeDownPhaseIndex[3]] / testToProcess3.get('resistance')[TimeDownPhaseIndex[2]]
                                 , '.m', label = 'test 3 - up2')
# x label and y label
CRatio2ResisRatio_ax.set_xlabel('Contraction Ratio')
CRatio2ResisRatio_ax.set_ylabel('Resistance Ratio')
# added these three lines
lns = lns1+lns2+lns3 + lns4+lns5+lns6
labs = [l.get_label() for l in lns]
CRatio2ResisRatio_ax.legend(lns, labs, loc=0)
# demo_ax.legend('Test Demo')
now = datetime.datetime.now()
title = 'CRatio2ResisRatio_fig' + now.strftime("_%b%d_%I%M") + '.png'
plt.savefig(title)
CRatio2ResisRatio_fig.show()


#############################################################################################################
# When we only focus on the single ramp up and part of it.
# Contraction Ratio Vs Resistance Ratio
Pressure2CRatio_fig, Pressure2CRatio_ax = plt.subplots()
lns1 = Pressure2CRatio_ax.plot(testToProcess1.get('pressure')[TimeRisePhaseIndex[0]:TimeRisePhaseIndex[1]],
            testToProcess1.get('CRatio')[TimeRisePhaseIndex[0]:TimeRisePhaseIndex[1]]
            , '.b', label = 'test 1 - up1')
lns2 = Pressure2CRatio_ax.plot(testToProcess1.get('pressure')[TimeDownPhaseIndex[2]:TimeDownPhaseIndex[3]],
        testToProcess1.get('CRatio')[TimeDownPhaseIndex[2]:TimeDownPhaseIndex[3]]
            , '.c', label = 'test 1 - up2')

lns3 = Pressure2CRatio_ax.plot(testToProcess2.get('pressure')[TimeRisePhaseIndex[0]:TimeRisePhaseIndex[1]],
            testToProcess2.get('CRatio')[TimeRisePhaseIndex[0]:TimeRisePhaseIndex[1]]
            , '.r', label = 'test 2 - up1')
lns4 = Pressure2CRatio_ax.plot(testToProcess2.get('pressure')[TimeDownPhaseIndex[2]:TimeDownPhaseIndex[3]],
        testToProcess2.get('CRatio')[TimeDownPhaseIndex[2]:TimeDownPhaseIndex[3]]
            , '.k', label = 'test 2 - up2')

lns5 = Pressure2CRatio_ax.plot(testToProcess3.get('pressure')[TimeRisePhaseIndex[0]:TimeRisePhaseIndex[1]],
            testToProcess3.get('CRatio')[TimeRisePhaseIndex[0]:TimeRisePhaseIndex[1]]
            , '.y', label = 'test 3 - up1')
lns6 = Pressure2CRatio_ax.plot(testToProcess2.get('pressure')[TimeDownPhaseIndex[2]:TimeDownPhaseIndex[3]],
        testToProcess3.get('CRatio')[TimeDownPhaseIndex[2]:TimeDownPhaseIndex[3]]
            , '.m', label = 'test 3 - up2')
# x label and y label
Pressure2CRatio_ax.set_xlabel('pressure')
Pressure2CRatio_ax.set_ylabel('Contraction Ratio')
# added these three lines
lns = lns1+lns2+lns3 + lns4+lns5+lns6
labs = [l.get_label() for l in lns]
Pressure2CRatio_ax.legend(lns, labs, loc=0)
# demo_ax.legend('Test Demo')
now = datetime.datetime.now()
title = 'Pressure2CRatio_fig' + now.strftime("_%b%d_%I%M") + '.png'
plt.savefig(title)
Pressure2CRatio_fig.show()

# Just one more example
fig, ax = plt.subplots()
lns1 = ax.plot(testToProcess1.get('time'), testToProcess1.get('PrescribedCtrRa'), '.r')
lns2 = ax.plot(testToProcess1.get('time')[TimeRisePhaseIndex[0]:TimeRisePhaseIndex[1]],
        testToProcess1.get('PrescribedCtrRa')[TimeRisePhaseIndex[0]:TimeRisePhaseIndex[1]], '.b')
ax.plot(testToProcess1.get('time')[TimeRisePhaseIndex[2]:TimeRisePhaseIndex[3]],
        testToProcess1.get('PrescribedCtrRa')[TimeRisePhaseIndex[2]:TimeRisePhaseIndex[3]], '.b')
ax.plot(testToProcess1.get('time')[TimeDownPhaseIndex[0]:TimeDownPhaseIndex[1]],
        testToProcess1.get('PrescribedCtrRa')[TimeDownPhaseIndex[0]:TimeDownPhaseIndex[1]], '.c')
ax.plot(testToProcess1.get('time')[TimeDownPhaseIndex[2]:TimeDownPhaseIndex[3]],
        testToProcess1.get('PrescribedCtrRa')[TimeDownPhaseIndex[2]:TimeDownPhaseIndex[3]], '.c')
fig.show()



