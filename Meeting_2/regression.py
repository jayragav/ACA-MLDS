# Data Preprocessing Template
# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Salary_Data.csv')
X = dataset.iloc[:, :-1].values # number of years of exp.
y = dataset.iloc[:, 1].values # salary column

# now we split the data into training and testing set, for now, since we have
# only 30 entries, a good split will be of one third.
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/3, random_state = 0)

# Feature Scaling
"""from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
sc_y = StandardScaler()
y_train = sc_y.fit_transform(y_train.reshape(-1,1))"""

# now we fit the SLR into the training set
# we use the LinearRegression class of a library from sklearn package
from sklearn.linear_model import LinearRegression
regressor = LinearRegression() # we don't need any params, read the doc for the same

# the method we will be using is the fit method
# press Ctrl+I to inspect the fit() method of the class
# regressor will learn the co-relations from the training datasets
regressor.fit(X_train, y_train)

# by doing this, your first ML model is ready!
# now let's predict the Test set results
# use the predict method of the class, use inspection to explore the params and manual
y_pred = regressor.predict(X_test)


# now we have made the predictions, and will now visualize the predictions
# x_axis will have the number of years of exp, y_axis will have the salary (predicted)
plt.scatter(X_train, y_train, color = 'red')
plt.plot(X_train, regressor.predict(X_train), color = 'blue')

#label the graph
plt.title('Salary vs Experience (Training set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')

# represent the end of the graph and show it
plt.show()

# now lets visualize the same for the test set
plt.scatter(X_test, y_test, color = 'red')
plt.plot(X_train, regressor.predict(X_train), color = 'blue')
plt.title('Salary vs Experience (Test set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()
