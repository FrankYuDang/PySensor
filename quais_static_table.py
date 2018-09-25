# Create a quasi_static_table
# convert the info structure into a dictionary
import scipy.io as spio
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib import rc
import  pickle


mat = spio.loadmat('tableShape.mat', struct_as_record=False, squeeze_me=True)
Shape= mat['tableShape']
# pressure = infoShape.get(pressure)
pressure= Shape[:,0]
ContractionRatio = Shape[:,1]
StretchRatio = Shape[:,2]
shapeTablePy = { 'pressure': pressure, 'ContractionRatio':ContractionRatio, 'StretchRatio':StretchRatio}
# print(shapeTablePy)

with open('shapeTablePy.pkl', 'wb') as f:
    # Pickle the dictionary using the highest protocol available
    pickle.dump(shapeTablePy, f, pickle.HIGHEST_PROTOCOL)

rc('font',**{'family':'serif','serif':['Times']})
rc('text', usetex=True)
plt.rcParams["font.family"] = "Times New Roman"
plt.rc('xtick', labelsize=8)
plt.rc('ytick', labelsize=8)
plt.rc('axes', labelsize=8)

# width as measured in inkscape
width = 3.4
height = width / 1.618


############ FIG 1
P2SR_fig, P2SR_ax = plt.subplots()
# set the edges of the subplots of the figure.
plt.subplots_adjust(left=.15, bottom=.20, right=.95, top=.95)

x = pressure[5:21]/1000
y = StretchRatio[5:21]
ln1 = plt.plot(x, y, '.b')

P2SR_ax.set_xlabel('Pressure (kPa)')
P2SR_ax.set_ylabel('Stretch Ratio ($\Lambda_1$)')

P2SR_ax.legend(['Stretch Ratio ($\Lambda_1$)'])
# ax.legend(ln1.get_label())
P2SR_fig.set_size_inches(width, height)
plt.savefig('P2SR.pdf')

############ FIG 2
P2CR_fig, P2CR_ax = plt.subplots()
# set the edges of the subplots of the figure.
plt.subplots_adjust(left=.15, bottom=.20, right=.95, top=.95)

x = pressure[5:21]/1000
y = ContractionRatio[5:21]
ln2 = plt.plot(x, y, '.k')

P2CR_ax.set_xlabel('Pressure (kPa)')
P2CR_ax.set_ylabel('Contraction Ratio ($\Lambda_2$)')

P2CR_ax.legend(['Contraction Ratio ($\Lambda_2$)'])
# ax.legend(ln1.get_label())
P2CR_fig.set_size_inches(width, height)
plt.savefig('P2CR.pdf')

############ FIG 3
SR2CR_fig, SR2CR_ax = plt.subplots()
# set the edges of the subplots of the figure.
plt.subplots_adjust(left=.15, bottom=.20, right=.95, top=.95)

x = StretchRatio[5:21]
y = ContractionRatio[5:21]
ln3 = plt.plot(x, y, '.r')

SR2CR_ax.set_xlabel('Stretch Ratio ($\Lambda_1$)')
SR2CR_ax.set_ylabel('Contraction Ratio ($\Lambda_2$)')

SR2CR_ax.legend(['$\Lambda_2$, a function of $\Lambda_1$'])
# ax.legend(ln1.get_label())
SR2CR_fig.set_size_inches(width, height)
plt.savefig('SR2CR.pdf')
