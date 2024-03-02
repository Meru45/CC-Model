import deepchem as dc

from deepchem.data.datasets import ImageDataset
import matplotlib.pyplot as plt

import os
import shutil

path = './data/malaria/Parasitized/'
dir_list = os.listdir(path)
pathnew = './data/malarianew/Parasitized/'
print(len(dir_list))

for i in dir_list:
    print(i)
    shutil.move(path+i, pathnew+i)