import seaborn as sb

from cluster.dbscan import DBSCAN


model = DBSCAN(matrix, eps=0.6, min_samples=5)
clusters = model.clusters()
import pdb;pdb.set_trace()
