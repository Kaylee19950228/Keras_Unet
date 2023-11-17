import h5py
import numpy as np


f = h5py.File('data.hdf5', 'r')

all_images = []
all_ILM = []
all_RPE = []
for k in f.keys():
    key = k
    v = f[key]
    s = list(v)
    #print(s)
    for k2 in v.keys():
        key = k2
        set_2 = v[key]
        set_3 = list(set_2)
        #print(set_3)
        for k3 in set_2.keys():
            key = k3
            BS = set_2[key]
            BS_1 = list(BS)
            #print(BS_1)
            for k4 in BS.keys():
                key = k4
                scan = BS[key]
                scan_1 = list(scan)
                img = scan["IMG"]
                ILM = scan["Layer-ILM"]
                RPE = scan["Layer-RPE"]
                img_array = img[:]
                all_images.append(img_array)
                ILM_array = ILM[:]
                all_ILM.append(ILM_array)
                RPE_array = RPE[:]
                all_RPE.append(all_RPE)
                #print(img_array)


all_images=np.array(all_images)
all_ILM=np.array(all_ILM)
all_RPE=np.array(all_RPE)
print(all_images)

# all_images = np.array(all_images)
# print(all_images)
                # print(img_array.shape)
                # print(img)
                # print(scan_1)
                # plt.imshow(np.transpose(img_array), cmap=cm.gray)
                # plt.show()




