import logging

from gensim.models import Word2Vec

from utils.corenlp import StanfordCoreNLP

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)


if __name__ == '__main__':
    with open('datasets/stopwords.txt', 'r') as f:
        stopwords = set(map(lambda data: data.strip(), f.readlines()))
    with open('datasets/training_data.txt', 'r') as f:
        comments = map(lambda comment: comment.strip(), f.readlines())

    nlp = StanfordCoreNLP('http://localhost:9000')

    segments = []
    for comment in comments:
        output = nlp.annotate(comment, properties={'annotators': 'ssplit', 'outputFormat': 'json'})

        tokens = []
        for token in output["sentences"][0]['tokens']:
            if token['word'] not in stopwords:
                tokens.append(token['word'])
        segments.append(tokens)

    model = Word2Vec(segments, min_count=5, size=50, window=3, workers=8)
    model.wv.save_word2vec_format("datasets/vectors.txt", binary=False)
