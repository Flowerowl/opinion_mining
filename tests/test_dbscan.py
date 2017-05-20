import seaborn as sb

from cluster.dbscan import DBSCAN

matrix = [
    [1, 2, 3, 4, 5],
] * 100

model = DBSCAN(matrix, eps=0.6, min_samples=5)
clusters = model.clusters()
