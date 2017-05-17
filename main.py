import re

from collections import Counter


def generate_candidate_tags():
    with open('datasets/stopwords.txt', 'r') as f:
        stopwords = map(lambda data: data.strip(), f.readlines())

    with open('data/training_data.txt', 'r') as f:
        reviews = f.readlines()
        # remove non-chinese
        reviews = map(lambda review: ''.join(re.findall("([\u4E00-\u9FD5a-zA-Z0-9+#&\._]+)", review)), reviews)
        # remove stopwords
        reviews = map(lambda review: ''.join(list(filter(lambda word: word not in stopwords, jieba.cut(review)))), reviews)
        # pos tagging
        reviews = map(lambda review: pseg.cut(review), reviews)
        return reviews


def extract_aspects(reviews):
    aspects = Counter()
    prev_word = ''
    prev_tag = ''
    curr_word = ''

    for review in reviews:
        for word, tag in review:
            if tag == 'n':
                aspects[word] += 1
                #  aspects.append(word)
            #  if tag == 'n':
                #  if prev_tag == 'n':
                    #  curr_word = '%s %s' % (prev_word, word)
                #  else:
                    #  aspects.append(prev_word)
                    #  curr_word = word
            #  prev_word = curr_word
            #  prev_tag = tag

    #  aspects = list(filter(lambda x: aspects.count(x) > 100, aspects))
    import pdb; pdb.set_trace()


if __name__ == '__main__':
    reviews = pre_processing_reviews()
    aspects = extract_aspects(reviews)
