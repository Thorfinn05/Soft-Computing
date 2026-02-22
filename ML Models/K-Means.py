from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.cluster import KMeans

X, y = load_iris(return_X_y=True)

kmeans = KMeans(n_clusters=3, random_state=42)
y_pred = kmeans.fit_predict(X)

sns.heatmap(confusion_matrix(y, y_pred), annot=True)
plt.show()

X_vis = X[:, :2]
y_pred = kmeans.fit_predict(X_vis)

plt.scatter(X_vis[y_pred == 0, 0], X_vis[y_pred == 0, 1], c='salmon', label='Cluster 1')
plt.scatter(X_vis[y_pred == 1, 0], X_vis[y_pred == 1, 1], c='lightblue', label='Cluster 2')
plt.scatter(X_vis[y_pred == 2, 0], X_vis[y_pred == 2, 1], c='lightgreen', label='Cluster 3')

plt.scatter(kmeans.cluster_centers_[:, 0],
            kmeans.cluster_centers_[:, 1],
            marker="*", c='black', label='centroids')

plt.title('K-Means Clustering (Iris Sepal Features)')
plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')
plt.legend(); plt.grid(); plt.show()