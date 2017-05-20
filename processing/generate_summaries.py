from functools import partial
from operator import is_not

from cluster.dbscan import DBSCAN

def word2vec(candidate_tags, vectors, sentiment_words):
    vecs = []

    for tag in candidate_tags:
        vec = []
        for word in tag:
            vec.append(vectors.get(word))
            contain_sentiment = True if word in sentiment_words else False

        vec = list(filter(partial(is_not, None), vec))
        if vec and contain_sentiment:
            vec = [sum(item)/len(vec) for item in zip(*vec)]
            vecs.append({
                'text': ''.join(tag),
                'vector': vec,
            })
    return vecs


if __name__ == '__main__':
    with open('datasets/candidate_tags.txt', 'r') as f:
        candidate_tags = list(map(lambda tag: tag.strip().split(','), f))
    with open('datasets/vectors.txt', 'r') as f:
        vectors = dict(list(map(lambda vector: (vector.split()[0], list(map(float, vector.strip().split()[1:]))), f.readlines()[1:])))
    with open('datasets/sentimentwords.txt', 'r') as f:
        sentiment_words = list(map(lambda word: word.strip(), f))

    vecs = word2vec(candidate_tags, vectors, sentiment_words)
    text = [vec['text'] for vec in vecs]
    points = [vec['vector'] for vec in vecs]

    model = DBSCAN(points, eps=0.9, min_samples=5)
    clusters = model.clusters()
    for index, cluster_id in enumerate(clusters):
        with open(f'datasets/clusters/{cluster_id}.txt', 'a') as f:
            f.write(f"{text[index]}\n")
