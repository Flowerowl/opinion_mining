from functools import partial
from operator import is_not


def word2vec(candidate_tags, vectors, sentiment_words):
    vecs = []
    contain_sentiment = False

    for tag in candidate_tags:
        vec = []
        for word in tag:
            vec.append(vectors.get(word))
            if word in sentiment_words:
                contain_sentiment = True

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
