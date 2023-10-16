import cv2 as cv
import numpy as np

from skimage.feature import hog
from sklearn.model_selection import train_test_split as tts
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.externals import joblib

# read the image
img = cv.imread('digits.png')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# break up the image into individual digits
cells = [np.hsplit(row, 100) for row in np.vsplit(gray, 50)]

# compute the HOG feature for each digit and make a dataset
dataset = []
for i in range(50):
    for j in range(100):
        feature = hog(cells[i][j],
                      pixels_per_cells=(10, 10),
                      cells_per_block=(1, 1))
        dataset.append(feature)
dataset = np.array(dataset, 'float64')

# make labels for all 5000 digits
labels = []
for i in range(10):
    labels = labels + [i] * 500

# KNN algorithms
clf = KNeighborsClassifier()
x_train, x_test, y_train, y_test = tts(dataset, labels, test_size=0.3)
clf.fit(x_train, y_train)

# print accuracy score
print('Accuracy: ', accuracy_score(y_test, clf.predict(x_test)))

# save model
joblib.dump(clf, 'digit_classifier_knn.model')