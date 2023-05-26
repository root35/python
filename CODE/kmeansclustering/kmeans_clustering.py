import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn import datasets
import pandas as pd
import numpy as np

iris = datasets.load_iris()

X = pd.DataFrame(iris.data)
X.columns = ['sepal_length',
             'sepal_width',
             'petal_length',
             'petal_width']

y = pd.DataFrame(iris.target)
y.columns = ['Targets']

model = KMeans(n_clusters = 3)
model.fit(X)

print(model.labels_)

# colormap = red maps with 1st label in model.labels_,
#            blue with 2d label...
colormap = np.array(['red', 'blue', 'green'])

plt.scatter(X.petal_length,
            X.petal_width,
            c = colormap[model.labels_],
            s = 40)
plt.title('KMeans Clusters')
plt.show()

plt.scatter(X.petal_length,
            X.petal_width,
            c = colormap[y.Targets],
            s = 40)
plt.title('Actual Clusters')
plt.show()
