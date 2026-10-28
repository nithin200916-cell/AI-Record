from sklearn import datasets
import numpy as np
iris=datasets.load_iris()
x=iris.data
y=iris.target
print("features:",x)
print("target:",y)
