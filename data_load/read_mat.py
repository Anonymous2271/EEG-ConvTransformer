# encoding: utf-8
"""
 @author: Xin Zhang
 @contact: 2250271011@email.szu.edu.cn
 @time: 2022/11/15 14:59
 @name: 
 @desc:
"""

import numpy as np
import scipy.io
import pandas as pd
from matplotlib import pyplot as plt

category = {1: 'Human Body',
            2: 'Human Face',
            3: 'Animal Body',
            4: 'Animal Face',
            5: 'Fruit Vegetable',
            6: 'Inanimate Object'}


def read_locs_mat(path='D:/GitHub/EEG-ConvTransformer/data_load/electrodes_locations/Neuroscan_locs_orig.mat'):
    mat = scipy.io.loadmat(path)['A']
    # [64, 3]
    # x = mat[:, 0]
    # y = mat[:, 1]
    # z = mat[:, 2]
    # plt.scatter(x, y, z)
    # plt.show()
    return mat[:-2, :]  # [62, 3]


def read_locs_xlsx(path='D:/GitHub/EEG-ConvTransformer/data_load/electrodes_locations/GSN-HydroCel-128.xlsx'):
    table = pd.read_excel(path, skiprows=1, index_col=0)
    # print(np.shape(table.values[:-3, :]))  # [124 3]
    # x = table.values[:, 0]
    # y = table.values[:, 1]
    # z = table.values[:, 2]
    # plt.scatter(x, y, z)
    # plt.show()
    return table.values[:-3, :]  # [124, 3]


def read_eeg_mat(filepath='E:/Datasets/Stanford_digital_repository/S1.mat'):
    mat = scipy.io.loadmat(filepath)
    n_samples = np.asarray(mat['T']).squeeze()  # around 5184
    t_length = np.asarray(mat['N']).squeeze()  # time length of each sample, 32 always
    channels = 124

    X_3D = np.asarray(mat['X_3D'])
    assert (channels, t_length, n_samples) == np.shape(X_3D)
    # down-sample due to there are 124 channels while only 64 channel locations.
    # You don't need to do this if you can download the 128 channel locations from:
    #                  ftp://ftp.egi.com/pub/support/Documents/net_layouts/hcgsn_128.pdf
    # Please send me the copy if you get above PDF, thanks.
    # X_3D = X_3D[::2, :, :].transpose(2, 1, 0)  # [n_samples=5184, t_length=32, channels=62]
    X_3D = np.transpose(X_3D, (2, 1, 0))  # [n_samples=5184, t_length=32, channels=124]

    labels = np.asarray(mat['categoryLabels']).squeeze()  # [5184]
    assert len(labels) == len(X_3D)
    return X_3D, labels


if __name__ == '__main__':
    read_locs_xlsx()

    # return a dict
    # mat = scipy.io.loadmat('G:/Datasets/Stanford_digital_repository/S1.mat')
    # print(mat.keys(), '\n')
    # print(mat['__header__'], '\n')
    # print(mat['__version__'], '\n')
    # print(mat['__globals__'], '\n')
    # print('sub: ', mat['sub'])
    # print('Fs: ', mat['Fs'])
    # print('N: ', mat['N'], '\n')
    # print('T: ', mat['T'], '\n')
    # print('exemplarLabels: ', mat['exemplarLabels'], '\n')
    # print('categoryLabels: ', mat['categoryLabels'], '\n')
    # print('X_2D: ', np.shape(mat['X_2D']), '\n')
    # print('X_3D: ', np.shape(mat['X_3D']), '\n')  # [124 32 5188]
