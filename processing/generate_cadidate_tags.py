def generate_candidate_tags():
    with open('datasets/stopwords.txt', 'r') as f:
        stopwords = map(lambda data: data.strip(), f.readlines())


if __name__ == '__main__':
    generate_candidate_tags()
