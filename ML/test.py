#coding=utf-8
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.decomposition import PCA

import warnings


def show_some_sample_images(dataset, k=1):
    '''
        Shows k random image samples from dataset.

        In the train dataset, there are 728 columns that represent the image.
        We need to reshape this 728 x 1 array to 28 x 28, in order to plot the image correctly.
        You can see it at line: "img.reshape((28, 28))"

        :param dataset: Pandas DataFrame
        :param k: Number of images to be shown
    '''
    sample = dataset
    for index in range(k):
        img = sample.iloc[index].as_matrix()
        img = img.reshape((28, 28))
        plt.figure(figsize=(20, 2))
        plt.grid(False)
        plt.axis('off')
        plt.xticks([])
        plt.yticks([])
        plt.imshow(img)
        plt.show()
train = pd.read_csv('D:/zcw/train.csv')
#test = pd.read_csv('D:/zcw/test.csv')

labels = train.iloc[:, :1]
images = train.iloc[:, 1:]
# im=images.sample(1)
# show_some_sample_images(im)
pca=PCA(n_components=60,whiten=True)
new_images=pca.fit_transform(images)
# new_im=pca.inverse_transform(new_images)

train_images, test_images, train_labels, test_labels =train_test_split(new_images,labels,train_size=0.8,random_state=0)

clf=svm.SVC(kernel='rbf',C=300)
clf.fit(train_images,train_labels.values.ravel())
#linear 0.9145
#rbf 0.1105
#sigmoid 0.1105
#poly 0.952

print clf.score(test_images,test_labels)