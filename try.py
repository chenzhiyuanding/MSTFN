from ast import operator
import cv2
import numpy as np
import torch
aa= np.array([[0.1,0.2,0.3,0.2],[0.6,0.2,0.3,0.2]])
bb=torch.from_numpy(aa)
cc=bb.numpy()
for i in range(len(cc)):
    print(cc[i].argmax())
print()