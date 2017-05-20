import math

UNCLASSIFIED = False
NOISE = None

class DBSCAN(object):
    def __init__(self, points, eps=0.9, min_samples=5):
        if eps < 0.0:
            raise ValueError("eps must be positive.")
        if min_samples < 0:
            raise ValueError("min_samples must be positive.")
        self.eps = eps
        self.min_samples = min_samples
        self.points=points
        self.classes = [UNCLASSIFIED] * len(self.points)

    def clusters(self):
        cluster_id = 1
        for point_id, point in enumerate(self.points):
            if self. classes[point_id] == UNCLASSIFIED and self.expand_cluster(point_id, cluster_id):
                cluster_id += 1
        return self.classes

    def expand_cluster(self, point_id, cluster_id):
        seeds = self.get_neighbors(point_id)
        if len(seeds) < self.min_samples:
            self.classes[point_id] = NOISE
            return False
        else:
            self.classes[point_id] = cluster_id
            for seed_id in seeds:
                self.classes[seed_id] = cluster_id
                neighbors = self.get_neighbors(seed_id)
                if len(neighors) >= self.min_samples:
                    for


    def get_neighbors(self, point_id):
        seeds = []
        for _id, point in enumerate(self.points):
            if self.distance(self.points[point_id], point) >= self.eps:
                seeds.append(_id)
        return seeds

    def distance(self, v1, v2):
        numerator = sum([i*j for i,j in zip(v1, v2)])
        denominator = math.sqrt(sum([i*j for i,j in zip(v1, v1)])) * math.sqrt(sum([i*j for i,j in zip(v2, v2)]))

        if denominator == 0:
            raise
        return numerator/denominator
