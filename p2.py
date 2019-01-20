import matplotlib.pyplot as plt

from sklearn import datasets
from sklearn import svm

#Getting data to test
digits = datasets.load_digits()

#Algorithm used, gamma = 'size of leap(refer to yt tutorial p.2)'
clf = svm.SVC(gamma=0.0001, C=100)

#Printing length of dataset
print(len(digits.data))

#Training based on dataset
x,y = digits.data[:-10], digits.target[:-10]
clf.fit(x,y)

#Printing and predicting
print 'Prediction: ',clf.predict(digits.data[-6])

#Showing the prediction using matplotlib
plt.imshow(digits.images[-6], cmap=plt.cm.gray_r, interpolation="nearest")
plt.show()
