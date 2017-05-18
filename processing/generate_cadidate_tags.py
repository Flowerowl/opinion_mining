from utils.corenlp import StanfordCoreNLP

#  def generate_candidate_tags():
    #  with open('datasets/stopwords.txt', 'r') as f:
        #  stopwords = map(lambda data: data.strip(), f.readlines())

with open('datasets/training_data.txt', 'r') as f:
    reviews = f.readlines()

if __name__ == '__main__':
    #  generate_candidate_tags()
    nlp = StanfordCoreNLP('http://localhost:9000')
    text = "质量不错，大小合适，棉质的，很满意的，同事都问我好多钱在那买的，我是便宜，总之满意满意"

    output = nlp.annotate(text, properties={
        'annotators': 'tokenize,ssplit,pos,depparse,parse',
        'outputFormat': 'json'
    })
    dependecies = output['sentences'][0]['basicDependencies']
    for dep in dependecies:
        print(dep)
    import pdb;pdb.set_trace()
