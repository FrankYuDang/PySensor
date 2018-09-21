# Create a quasi_static_table
# convert the info structure into a dictionary
import scipy.io as spio
import matplotlib.pyplot as plt
import  pickle


mat = spio.loadmat('tableShape.mat', struct_as_record=False, squeeze_me=True)
Shape= mat['tableShape']
# pressure = infoShape.get(pressure)
pressure= Shape[:,0]
ContractionRatio = Shape[:,1]
StretchRatio = Shape[:,2]
shapeTablePy = { 'pressure': pressure, 'ContractionRatio':ContractionRatio, 'StretchRatio':StretchRatio}
print(shapeTablePy)

with open('shapeTablePy.pkl', 'wb') as f:
    # Pickle the dictionary using the highest protocol available
    pickle.dump(shapeTablePy, f, pickle.HIGHEST_PROTOCOL)
