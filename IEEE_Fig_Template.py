import numpy as np
import matplotlib as mpl
mpl.use('pdf')
import matplotlib.pyplot as plt

# plt.rc('font', family='serif', serif='Times')
# plt.rc('text', usetex=True)
plt.rcParams["font.family"] = "Times New Roman"
plt.rc('xtick', labelsize=8)
plt.rc('ytick', labelsize=8)
plt.rc('axes', labelsize=8)

# width as measured in inkscape
width = 3.487
height = width / 1.618

fig, ax = plt.subplots()
ax2 = ax.twiny()

# set the edges of the subplots of the figure.
plt.subplots_adjust(left=.15, bottom=.16, right=.99, top=.80)

x = np.arange(0.0, 3*np.pi , 0.1)
plt.plot(x, np.sin(x))

ax.set_ylabel('Some Metric (in unit)')
ax.set_xlabel('Something (in unit)')
ax.set_xlim(0, 3*np.pi)
ax.set_ylim(-1.0, 1.0)
fig.set_size_inches(width, height)

# Second X-axis
new_tick_location = np.array([2, 5, 7])

def tick_fucntion(x):
    V = 1/(1+x)
    return ["%.3f" % z for z in V]

ax2.set_xlim(ax.get_xlim())
ax2.set_xticks(new_tick_location)
ax2.set_xticklabels(tick_fucntion(new_tick_location))
ax2.set_xlabel(r"Modified x-axis: $1/(1+x)$")
plt.savefig('ploot2')
# plt.savefig('plot')
# plt.show()

