import pandas as pd
import numpy as np
import sklearn
from sklearn import linear_model
from sklearn.utils import shuffle
import pickle
import matplotlib.pyplot as pyplot
from matplotlib import style

# Import the data for training model
data = pd.read_csv("student-por.csv", sep =";")

# Defining data set
data = data[["G1","G2","G3","studytime","failures","absences"]]

# Defining prediction argument
predict = "G3"
p="studytime"
X = np.array(data.drop([predict] , 1))
Y = np.array(data[predict])

 # Defining the linear Regression model 
xtrain, xtest, ytrain, ytest = sklearn.model_selection.train_test_split(X,Y,test_size =0.02)

best_model= 0
# Finding the best model
for _ in range(100):
	xtrain, xtest, ytrain, ytest = sklearn.model_selection.train_test_split(X,Y,test_size =0.02)
	linear =linear_model.LinearRegression()
	linear.fit(xtrain,ytrain)# Finding the best fit line
	accuracy = linear.score(xtest,ytest)
	print(accuracy)
	
	if accuracy > best_model:
		best_model = accuracy
	# Pickle module for saving model
		with open("sm.pickle", "wb") as f:
			pickle.dump(linear, f)
	
# Pickle module for loading model
pickle_in = open("sm.pickle", "rb")
linear= pickle.load(pickle_in)

# predictions
predictions = linear.predict(xtest)
for x in range(len(predictions)):
	print(predictions[x],xtest[x],ytest[x])
	
# Graphing the scatter plot	
style.use("ggplot")
pyplot.scatter(data[p],data[predict])
pyplot.xlabel(f"Grade  {predict}")
pyplot.ylabel("Final Grade")
pyplot.show()