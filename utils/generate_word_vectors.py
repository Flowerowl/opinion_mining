import logging

from gensim.models import Word2Vec

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)


if __name__ == '__main__':
    with open('datasets/training_data.txt', 'r') as f:
        comments = map(lambda comment: comment.split(), f.readlines())

    model = Word2Vec(comments, min_count=5, size=50, window=3, workers=8)
    model.wv.save_word2vec_format("datasets/vectors.txt", binary=False)
