import h5py
import numpy as np
import matplotlib.pyplot as plt
import numpy.ma as npm


f = h5py.File('data.hdf5', 'r')
v = f["visit_3"]
s = v["subject_104"]
set_1 = s["set_2"]
B = set_1["BSCAN_1"]
img = B["IMG"]
ILM = B["Layer-ILM"]
RPE = B["Layer-RPE"]
img_array = img[:]
ILM_arraay = ILM[:]
RPE_array = RPE[:]


# # set = list(sub)
# # B= set["set_1"]
# # I = list(B)
# # imag = I["IMG"]
# print(imag)
x1 = np.arange(1536)
y1 = ILM_arraay[0][:]
y2 = RPE_array[0][:]
# print(img_array)
plt.imshow(np.transpose(img_array))
plt.plot(x1,y1,color = "green")
plt.plot(x1,y2,color = "red")
plt.show()

mask = img_array
arr = npm.array(img_array, mask = mask)
print(arr)
plt.imshow(np.transpose(arr))
plt.show()