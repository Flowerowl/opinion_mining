import jieba

with open('data/stopwords.txt', 'r') as f:
    stopwords = map(lambda data: data.strip(), f.readlines())

with open('data/dianping_reviews.txt', 'r') as f:
    reviews = f.readlines()
    reviews = map(lambda review: jieba.cut(review), reviews)
