# This is a sample of Simple Linear Regression model.

# Importing the libraries
import pandas as pd
import matplotlib.pyplot as plt

# Importing the dataset
experience_salary = pd.read_csv("Salary.csv")
X = experience_salary.iloc[:, :-1].values
y = experience_salary.iloc[:, 1].values

#Let's look at some statistical information about the dataframe
print(experience_salary.describe())

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test,y_train, y_test = train_test_split(X, y, train_size = 0.7, random_state = 0)

#import LinearRegression from sklearn
from sklearn.linear_model import LinearRegression
lr = LinearRegression()
lr.fit(X_train, y_train)

# Predicting the Test set results
y_pred = lr.predict(X_test)

#Mean_Squared_Error and R^2 value
from sklearn.metrics import mean_squared_error, r2_score
mse = mean_squared_error(y_test, y_pred)
r_squared = r2_score(y_test, y_pred)
print('Mean_Squared_Error :' ,mse)
print('r_square_value :' ,r_squared)

#Actual and predicted
c = [i for i in range(1,12)] #generating index
fig = plt.figure()
plt.plot(c,y_test, color ='blue', linewidth=2.5, linestyle='-')
plt.plot(c,y_pred, color ='red', linewidth=2.5, linestyle='-')
fig.suptitle('Actual and predicted',fontsize = 20) #plot heading
plt.xlabel('Year of Experience',fontsize = 18)                  #X-label
plt.ylabel('Salary', fontsize=16)             #y-label
plt.show()

#Error terms
c = [i for i in range(1,12)] #generating index
fig = plt.figure()
plt.plot(c,y_test-y_pred, color ='blue', linewidth=2.5, linestyle ="-")
fig.suptitle('Error Terms',fontsize = 20) #plot heading
plt.xlabel('Year of Experience',fontsize = 18)                  #X-label
plt.ylabel('ytest-ypred', fontsize=16)             #y-label
plt.show()

