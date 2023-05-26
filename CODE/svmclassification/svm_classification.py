from sklearn import svm
from sklearn import datasets

iris = datasets.load_iris()
X = iris.data[:,:2]  # first 2 columns/features only
y = iris.target

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                    test_size=0.2,
                                                    random_state=4)

model = svm.SVC(kernel='linear')
model.fit(X_train, y_train)

accuracy = model.score(X_test, y_test)
print(accuracy)
