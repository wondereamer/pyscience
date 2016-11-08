import matplotlib.pyplot as plt

from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs

plt.figure(figsize=(12, 12))

n_samples = 1500
random_state = 170
# [[x1, y1], [x2, y2], ..]
X, y = make_blobs(n_samples=n_samples, random_state=random_state)

## Incorrect number of clusters
y_pred = KMeans(n_clusters=3, random_state=random_state).fit_predict(X)

plt.subplot(221)
print y_pred
#colors = ['r' if cluster_id == 0 else 'b' for cluster_id in y_pred]
plt.scatter(X[:, 0], X[:, 1], c=y_pred)
#plt.scatter(X[:, 0], X[:, 1])
plt.title("Incorrect Number of Blobs")
plt.show()