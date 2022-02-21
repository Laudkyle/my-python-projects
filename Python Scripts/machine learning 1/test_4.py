import pandas as pd
import numpy as np
import sklearn
from sklearn import linear_model
from sklearn.utils import shuffle
import pickle
import matplotlib.pyplot as pyplot
from matplotlib import style

data = pd.read_csv("student-por.csv", sep =";")
data = data[["G1","G2","G3","studytime","failures","absences"]]
predict = "G3"
p="G1"
X = np.array(data.drop([predict] , 1))
Y = np.array(data[predict])
 
xtrain, xtest, ytrain, ytest = sklearn.model_selection.train_test_split(X,Y,test_size =0.02)

linear =linear_model.LinearRegression()
linear.fit(xtrain,ytrain)
accuracy = linear.score(xtest,ytest)
print(accuracy)

with open("sm.pickle", "wb") as f:
	pickle.dump(linear, f)

pickle_in = open("sm.pickle", "rb")
linear= pickle.load(pickle_in)

predictions = linear.predict(xtest)
for x in range(len(predictions)):
	print(predictions[x],xtest[x],ytest[x])
	
style.use("ggplot")
pyplot.scatter(data[p],data[predict])
pyplot.xlabel(f"Grade  {predict}")
pyplot.ylabel("Final Grade")
pyplot.show()