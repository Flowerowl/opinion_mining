class DBSCAN(object):
    def __init__(self, eps=0.9, min_samples=5):
        if eps < 0.0:
            raise ValueError("eps must be positive.")
        if min_samples < 0:
            raise ValueError("min_samples must be positive.")

        self.eps = eps
        self.min_samples = min_samples

    def cluster(self, points):
        pass

    def nearest_neighbors(self, radius=eps, ):
        pass

    def center(self, vectors):
        pass

    def write_cluster(self):
        pass
