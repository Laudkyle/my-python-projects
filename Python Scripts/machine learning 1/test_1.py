import pandas as pd
import numpy as np
import sklearn
from sklearn import linear_model
from sklearn.utils import shuffle
import matplotlib.pyplot as pyplot
import pickle
from matplotlib import style

# Reading the csv file using pandas
data = pd.read_csv("student-mat.csv", sep = ";")
print(data.head()) # Reading the first five elements of the data
data = data[["G1","G2","G3","studytime","failures","absences"]] # Defining the the parameters for predictions

print(data.head())
# Defining the prediction argument
predict = "failures"
p ="studytime"
X = np.array(data.drop([predict], 1))
y= np.array(data[predict])

x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size=0.05)
"""
best = 0
for _ in range(50):

    x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size=0.05)

    linear = linear_model.LinearRegression()
    linear.fit(x_train, y_train)
    acc= linear.score(x_test, y_test)
    print(acc)

    with open("sm.pickle", "wb") as f:
        pickle.dump(linear, f)
    if acc > best:
        best = acc"""

pickle_in = open("sm.pickle", "rb")
linear = pickle.load(pickle_in)


print("Coefficients : ", linear.coef_ )
print("Intercept : ", linear.intercept_)
predictions = linear.predict(x_test)

for x in range(len(predictions)):
    print(predictions[x], x_test[x], y_test[x])

style.use("ggplot")
pyplot.scatter(data[p],data["G3"])
pyplot.xlabel(p)
pyplot.ylabel("Final Grade")
pyplot.show()