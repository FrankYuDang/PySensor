# Noted: Sep 21 -

import os
import pickle
import numpy as np
from matplotlib import pyplot
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import myFunc

LoadSavedDataFolder = os.path.join('H:/netData/DynamicModel/jrvicon_data', 'R25T30GroupedData1809131632.pkl')
R = 40

timestamp = myFunc.timestamp(LoadSavedDataFolder)
TestSetting = myFunc.testsetting(LoadSavedDataFolder)


with open(LoadSavedDataFolder, 'rb') as f:
    MeasuredGroupedData = pickle.load(f)
TestName = [f for f in MeasuredGroupedData.keys()]

# Basic Statistic of Position
marker1 = MeasuredGroupedData.get('marker1')
marker1Info = {'raw' : marker1}
marker1Info.update({'mean': marker1.mean(axis=0)})
marker1Info.update({'std' : marker1.std(axis=0)})
marker1Info.update({'InitPos':marker1[50:200, :].mean(axis=0)})

# Pressure info
MeasuredSmoothP = MeasuredGroupedData.get('MeasuredSmoothP')
marker1Info.update({'MeasuredSmoothP':MeasuredSmoothP})
# Resistance info
Resistance1 = MeasuredGroupedData.get('r1Delta')
marker1Info.update({'Resistance1':Resistance1})
# PrescribeCtrRa info
PrescribeCtrRa = MeasuredGroupedData.get('PrescribeCtrRa')
marker1Info.update({'PrescribeCtrRa':PrescribeCtrRa})

ref1 = MeasuredGroupedData.get('ref1')
ref1Info = {'raw' : ref1}
ref1Info.update({'mean': ref1.mean(axis=0)})
ref1Info.update({'std' : ref1.std(axis=0)})
ref1Info.update({'InitPos':ref1.mean(axis=0)})

ref2 = MeasuredGroupedData.get('ref2')
ref2Info = {'raw' : ref2}
ref2Info.update({'mean': ref2.mean(axis=0)})
ref2Info.update({'std' : ref2.std(axis=0)})
ref2Info.update({'InitPos':ref2.mean(axis=0)})

ref3 = MeasuredGroupedData.get('ref3')
ref3Info = {'raw' : ref3}
ref3Info.update({'mean': ref3.mean(axis=0)})
ref3Info.update({'std' : ref3.std(axis=0)})
ref3Info.update({'InitPos':ref3.mean(axis=0)})

ref4 = MeasuredGroupedData.get('ref4')
ref4Info = {'raw' : ref4}
ref4Info.update({'mean': ref4.mean(axis=0)})
ref4Info.update({'std' : ref4.std(axis=0)})
ref4Info.update({'InitPos':ref4.mean(axis=0)})
# Plot the position
sequencePosX = [ marker1Info.get('InitPos')[0], ref1Info.get('InitPos')[0]]
sequencePosX.append(ref2Info.get('InitPos')[0])
sequencePosX.append(ref3Info.get('InitPos')[0])
sequencePosX.append(ref4Info.get('InitPos')[0])

sequencePosY = [ marker1Info.get('InitPos')[1], ref1Info.get('InitPos')[1]]
sequencePosY.extend( [ref2Info.get('InitPos')[1], ref3Info.get('InitPos')[1], ref4Info.get('InitPos')[1]])

sequencePosZ = [ marker1Info.get('InitPos')[2], ref1Info.get('InitPos')[2]]
sequencePosZ.extend( [ref2Info.get('InitPos')[2], ref3Info.get('InitPos')[2], ref4Info.get('InitPos')[2]])


centroid = (ref1Info.get('mean') + ref2Info.get('mean') + ref3Info.get('mean') + ref4Info.get('mean') )/4

# Plot the translational position in 3D
fig3D = pyplot.figure()
ax3D = Axes3D(fig3D)
colorPoint = ['b', 'r', 'c', 'm', 'y']
for num, cS in enumerate(colorPoint):
    ax3D.scatter(sequencePosX[num], sequencePosY[num], sequencePosZ[num], c = cS)
ax3D.scatter(centroid[0], centroid[1], centroid[2], c ='r')
k = 33
ax3D.set_title("3D position{} {}".format(timestamp, TestSetting))
fig3D.savefig("3D position{} {}".format(timestamp, TestSetting))


# Transform Coordination.
coordNew = marker1Info.get('raw') - centroid
marker1Info.update({'newcoord': coordNew})
vicon_marker_offset = 4
translationNew = np.sqrt(np.square(coordNew[:, 0]) + np.square(coordNew[:, 1])) + vicon_marker_offset
marker1Info.update({'RadialTransPos': translationNew})

CRatio = np.absolute((R-translationNew)/R)
CRatio_fig, CRatio_ax = plt.subplots()
CRatio_ax.plot(CRatio, '.b')
CRatio_fig.savefig("CRatio{} {}.png".format(timestamp, TestSetting))

marker1Info.update({'CRatio': CRatio})

# Create the canvas
trans_fig, trans_ax = plt.subplots()
trans_ax.plot(marker1Info.get('raw')[:,0], c='b')
trans_ax.set_title("RadialTransPos{} {}".format(timestamp, TestSetting))
trans_fig.savefig("RadialTransPos{} {}.png".format(timestamp, TestSetting))
PoseInfo = {'marker1Info':marker1Info, 'ref1Info':ref1Info, 'ref2Info':ref2Info,
            'ref3Info':ref3Info, 'ref4Info':ref4Info, 'centroid': centroid}

SaveFolder = LoadSavedDataFolder.strip('.pkl') + 'PoseInfo.pkl'
# Store data
with open(SaveFolder, 'wb') as f:
    # Pickle the dictionary using the highest protocol available
    pickle.dump([MeasuredGroupedData, PoseInfo], f, pickle.HIGHEST_PROTOCOL)


