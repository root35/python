import matplotlib.pyplot as plt
import pandas as pd


## LOADING DATA

dataset = pd.read_csv('50startups.csv')

X = dataset.iloc[:,:-1].values   # Independent variables
y = dataset.iloc[:,4].values     # Dependent variables


## TRANSFORMING DATA

from sklearn.preprocessing import LabelEncoder, OneHotEncoder

# Encoding 3d column: categorical variable
labelencoder = LabelEncoder()
X[:,3] = labelencoder.fit_transform(X[:,3])

onehotencoder = OneHotEncoder(categories=[3])
X = onehotencoder.fit_transform(X).toarray()


## SPLIT DATASET INTO TRAIN AND TEST

from sklearn.cross_validation import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                    test_size=0.2,
                                                    random_state=0)


## BUILD THE MODEL AND PREDICT

from sklearn.linear_model import LinearRegression

regressor = LinearRegression()
regressor.fit(X_train, y_train)

y_pred = regressor.predict(X_test)
print(y_pred)
print(y_test)

colors = ('red', 'blue')
plt.scatter(y_pred, y_test, c = colors)
plt.xlabel('y_pred')
plt.ylabel('y_test')
plt.show()


